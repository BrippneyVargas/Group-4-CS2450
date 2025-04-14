from pydantic import BaseModel
from typing import List, Optional


class Task(BaseModel):
    """
    Class that handle details needed for each task to be added

    Attributes:
        - title: str - title of the task
        - description: str - description of the task
        - priority: int - level of priority (1:high, 2:medium, 3:low)
        - tag: str - A tag to categorize the task
    """

    id: Optional[int]
    title: str
    description: str
    priority: int
    tag: str

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "tag": self.tag,
        }


class TaskManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.task_list: List[Task] = []

    def add_task(self, task: Task) -> None:
        self.task_list.append(task)

    def load_tasks(self) -> None:
        """
        Load tasks from the database using the provided connection manager.
        This function reads all tasks from the SQL database and inputs the list of
        Task objects into the task_list class variable.
        """
        self.task_list = self.db_manager.load_all()

    def save_tasks(self) -> None:
        """
        Save tasks from the task_list object to the SQL database.
        """
        response = self.db_manager.save_tasks(self.task_list)
        if not response:
            print("Error: Failed to save tasks to the database.")
