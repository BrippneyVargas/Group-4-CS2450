from tabulate import tabulate
from typing import List
from task import Task
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

    def save_tasks(self) -> None:
        task_data = [task.to_dict() for task in self.tasks]
        with open("tasks.json", "rw"):
            json.dumps(task_data, indent=4)

    def load_tasks(self) -> None:
        pass

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        # Convert list of Task objects into a list of dictionaries
        task_list = [task.to_dict() for task in self.tasks]

        # Use tabulate to format the output
        print(tabulate(task_list, headers="keys", tablefmt="fancy_grid"))


tm = TaskManager()
tm.add_task("test", "test", 1)
tm.display_tasks()
