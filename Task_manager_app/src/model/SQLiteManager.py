from model.DatabaseManager import DatabaseManager
import sqlite3
from model.Task import *

class SQLiteManager(DatabaseManager):
    def __init__(self, db_name: str) -> None:
        self.__conn = sqlite3.connect(db_name)
        self.__tasks = []

        self.__make_task_db()
        self.__make_user_db()
        self.__make_task_user_db()

        self.load_all()

    def __make_task_db(self, table_name: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS task (
                task_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                title VARCHAR(64),
                description VARCHAR(256),
                priority_id TINYINT UNSIGNED NOT NULL,
                tag_id TINYINT UNSIGNED NOT NULL,
                status_id TINYINT UNSIGNED NOT NULL,
                PRIMARY KEY (task_id)
            );
            '''
        )
        cursor.commit()
        cursor.close()
        
    def __make_user_db(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS user (
                user_id TINYINT UNSIGNED NOT NULL,
                email VARCHAR(64),
                PRIMARY KEY (user_id)
            );
            '''
        )
        cursor.commit()
        cursor.close()

    def __make_task_user_db(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS task_user (
                task_id UNSIGNED NOT NULL,
                user_id UNSIGNED NOT NULL,
                PRIMARY KEY (task_id, user_id),
                CONSTRAINT fk_task_user_task FOREIGN KEY (task_id) REFERENCES task (task_id) ON DELETE RESTRICT ON UPDATE CASCADE,
                CONSTRAINT fk_task_user_user FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE RESTRICT ON UPDATE CASCADE
            );
            '''
        )
        cursor.commit()
        cursor.close()

    def load_all(self) -> None:
        cursor = self.__conn.cursor()
        self.__tasks = cursor.fetchall()
        cursor.close()

    def save_task(self, task: Task) -> None:
        cursor = self.__conn.cursor
        if task["task_id"] in self.__tasks["task_id"]:
            cursor.execute(
                '''
                UPDATE task
                SET
                    title = %s,
                    description = %s,
                    priority_id = %s,
                    tag_id = %s
                WHERE task_id = %s;
                ''' %
                    task["title"],
                    task["description"],
                    str(task["priority_id"]),
                    str(task["tag_id"]),
                    str(task["task_id"])
            )
        else:
            cursor.execute(
                '''
                INSERT INTO task
                VALUES(%s, %s, %s, %s);
                ''' %
                    task["title"],
                    task["description"],
                    str(task["priority_id"]),
                    str(task["tag_id"])
            )
