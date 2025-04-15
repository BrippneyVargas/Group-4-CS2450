from model.Task import Task
from typing import List
import sqlite3


class SQLiteManager:
    """SQLite Connection Manager using Singleton design pattern."""

    __instance = None

    def __new__(cls, *args, **kwargs):
        # Return the existing instance if it exists; otherwise, create one
        if cls.__instance is None:
            cls.__instance = super(SQLiteManager, cls).__new__(cls)
        return cls.__instance

    def __init__(self, db_name: str) -> None:
        # Use a flag to ensure that initialization happens only once
        if hasattr(self, "_initialized") and self._initialized:
            return

        # Connect to the SQLite database file
        self.__conn = sqlite3.connect(db_name, check_same_thread=False)
        self.__conn.execute("PRAGMA foreign_keys = ON;")

        # Create the tables if they don't exist already
        self.__make_task_table()
        self.__make_user_table()
        self.__make_task_user_table()

        # Mark the instance as initialized
        self._initialized = True

    def __make_task_table(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS task (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                priority INTEGER NOT NULL,
                tag TEXT NOT NULL,
                active BOOLEAN,
                completed BOOLEAN
            );
            """
        )
        self.__conn.commit()
        cursor.close()

    def __make_user_table(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user (
                user_id INTEGER PRIMARY KEY,
                email TEXT,
                password_hash TEXT
            );
            """
        )
        self.__conn.commit()
        cursor.close()

    def __make_task_user_table(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS task_user (
                task_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                PRIMARY KEY (task_id, user_id),
                FOREIGN KEY (task_id) REFERENCES task (task_id) ON DELETE RESTRICT ON UPDATE CASCADE,
                FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE RESTRICT ON UPDATE CASCADE
            );
            """
        )
        self.__conn.commit()
        cursor.close()

    def load_all_active(self) -> List[Task]:
        """
        Loads all tasks from the database, converts them into Task objects,
        and updates the manager's internal task list.

        Returns:
            List[Task]: A list of Task objects.
        """
        cursor = self.__conn.cursor()
        # Select all columns from the task table.
        cursor.execute(
            """
            SELECT task_id, title, description, priority, tag, active, completed
            FROM task
            WHERE active = 1;
            """
        )
        rows = cursor.fetchall()
        tasks: List[Task] = []

        for row in rows:
            # Assuming the ordering is: task_id, title, description, priority, tag, active, completed
            task = Task(
                title=row[1], description=row[2], priority=row[3], tag=row[4], active=row[5], completed=row[6], id=row[0]
            )
            tasks.append(task)

        cursor.close()
        return tasks

    def save_tasks(self, task_list: List[Task]) -> bool:
        """
        Saves the current list of tasks to the database.
        For each task in task_list, if task.to_dict() returns a dictionary containing
        a non-null 'task_id', it updates the record in the task table.
        Otherwise, it inserts a new record and updates the task instance with the new task_id.

        Returns:
            bool: True if all tasks are successfully saved, False otherwise.
        """
        try:
            cursor = self.__conn.cursor()
            for task in task_list:
                data = task.to_dict()  # Expected keys: task_id, title, description, priority, tag
                if data.get("id") is not None:  # Task already exists in the DB; update it.
                    cursor.execute(
                        """
                        UPDATE task
                        SET title = ?, description = ?, priority = ?, tag = ?, active = ?, completed = ?
                        WHERE task_id = ?
                        """,
                        (
                            data["title"],
                            data["description"],
                            data["priority"],
                            data["tag"],
                            data["active"],
                            data["completed"],
                            data["id"],
                        ),
                    )
                else:
                    # Insert new task. SQLite will assign a new task_id automatically.
                    cursor.execute(
                        """
                        INSERT INTO task (title, description, priority, tag, active, completed)
                        VALUES (?, ?, ?, ?, ?, ?)
                        """,
                        (data["title"], data["description"], data["priority"], data["tag"], data["active"], data["completed"]),
                    )
                    # Update the task object with the new task_id from SQLite.
                    task.id = cursor.lastrowid

            self.__conn.commit()
            cursor.close()
            return True
        except Exception as e:
            self.__conn.rollback()
            print("ERROR: There was a problem while saving the tasks to the database:", e)
            return False
