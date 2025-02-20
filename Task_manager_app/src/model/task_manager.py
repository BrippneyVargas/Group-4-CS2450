from tabulate import tabulate
from typing import List
from .task import Task
import json


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, desc: str, priority: int) -> None:
        """Create a new task and add it to the list of tasks

        Args:
            title (str): The title of the task. This should be unique!
            desc (str): A brief description of the task.
            priority (int): A number expressing the priority of the task. Higher numbers are higher priority.
        """
        self.tasks.append(Task(title, desc, priority))
        return

    def delete_task(self, task_to_delete: Task) -> None:
        """Remove a task from the task list by the task name.

        Args:
            task_to_delete (Task): The task you want to remove.
        """
        for i, task in enumerate(self.tasks):
            if task_to_delete.title == task.title:
                del self.tasks[i]
                break

    def save_tasks(self, file_path: str) -> None:
        task_data = [task.to_dict() for task in self.tasks]
        with open(file_path, "w") as f:
            json.dump(task_data, f, indent=4)

    def load_tasks(self, file_path: str) -> None:
        with open(file_path, "r") as f:
            task_data = json.load(f)
        for task in task_data:
            self.add_task(task["Title"], task["Description"], task["Priority"])

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        # Convert list of Task objects into a list of dictionaries
        task_list = [task.to_dict() for task in self.tasks]

        # Use tabulate to format the output
        print(tabulate(task_list, headers="keys", tablefmt="fancy_grid"))


tm = TaskManager()
tm.add_task("test", "test", "test")
tm.save_tasks("tasks.json")
