import sqlite3
from typing import List, Optional
from model.Task import Task

class SQLiteManager:
    def __init__(self, db_name: str) -> None:
        # Use check_same_thread=False if you plan on accessing this connection from multiple threads (common with FastAPI).
        self.__conn = sqlite3.connect(db_name, check_same_thread=False)
        self.__conn.row_factory = sqlite3.Row  # so we can access columns by name
        self.__create_tables()

    def __create_tables(self) -> None:
        cursor = self.__conn.cursor()
        # Create the main task table.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS task (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority INTEGER NOT NULL,
                tag TEXT,
                status INTEGER NOT NULL DEFAULT 0
            );
        """)
        # Optionally, create additional tables (user, task_user) if needed.
        self.__conn.commit()
        cursor.close()

    def get_all_tasks(self) -> List[Task]:
        cursor = self.__conn.cursor()
        cursor.execute("SELECT * FROM task")
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append(
                Task(
                    id=row["task_id"],
                    title=row["title"],
                    description=row["description"],
                    priority=row["priority"],
                    tag=row["tag"],
                    status=row["status"],
                )
            )
        cursor.close()
        return tasks

    def get_task(self, task_id: int) -> Optional[Task]:
        cursor = self.__conn.cursor()
        cursor.execute("SELECT * FROM task WHERE task_id = ?", (task_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Task(
                id=row["task_id"],
                title=row["title"],
                description=row["description"],
                priority=row["priority"],
                tag=row["tag"],
                status=row["status"],
            )
        return None

    def add_task(self, task: Task) -> Task:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO task (title, description, priority, tag, status)
            VALUES (?, ?, ?, ?, ?)
        """,
            (task.title, task.description, task.priority, task.tag, getattr(task, "status", 0)),
        )
        self.__conn.commit()
        task.id = cursor.lastrowid
        cursor.close()
        return task

    def update_task(self, task: Task) -> bool:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            UPDATE task
            SET title = ?, description = ?, priority = ?, tag = ?, status = ?
            WHERE task_id = ?
        """,
            (task.title, task.description, task.priority, task.tag, getattr(task, "status", 0), task.id),
        )
        self.__conn.commit()
        updated = cursor.rowcount > 0
        cursor.close()
        return updated

    def delete_task(self, task_id: int) -> bool:
        cursor = self.__conn.cursor()
        cursor.execute("DELETE FROM task WHERE task_id = ?", (task_id,))
        self.__conn.commit()
        deleted = cursor.rowcount > 0
        cursor.close()
        return deleted
