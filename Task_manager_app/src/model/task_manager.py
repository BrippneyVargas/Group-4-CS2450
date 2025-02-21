from typing import List, Literal
from tabulate import tabulate
from .task import Task
import json


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self.unsaved_changes: bool = False

    def add_task(self, title: str, desc: str, priority: Literal[1, 2, 3]) -> None:
        """Create a new task and add it to the list of tasks

        Args:
            title (str): The title of the task. This should be unique!
            desc (str): A brief description of the task.
            priority (int): A number expressing the priority of the task. Higher numbers are higher priority.
        """
        if priority not in [1, 2, 3]:
            raise ValueError("Priority must be 1, 2, or 3")
        self.tasks.append(Task(title, desc, priority))
        return

    def delete_task(self, task_title_to_delete: str) -> None:
        """Remove a task from the task list by the task name.

        Args:
            task_to_delete (Task): The task you want to remove.
        """
        for i, task in enumerate(self.tasks):
            if task_title_to_delete == task.title:
                del self.tasks[i]
                break
        print("Task not found.")  # If the task is not found it will reach this and print to warn the user.

    def save_tasks(self, file_path: str) -> None:
        task_data = [task.to_dict() for task in self.tasks]
        with open(file_path, "w") as f:
            json.dump(task_data, f, indent=4)

    def load_tasks(self, file_path: str) -> None:
        """Loads tasks from a JSON file with error handling."""
        try:
            with open(file_path, "r") as f:
                task_data = json.load(f)  # This will raise `json.JSONDecodeError` if the JSON is invalid

            if not isinstance(task_data, list):  # Ensure it's a list of tasks
                raise ValueError("Invalid JSON format: Expected a list of tasks.")

            for task in task_data:
                if not all(k in task for k in ("Title", "Description", "Priority")):
                    raise KeyError("Missing required keys in task entry.")

                self.add_task(task["Title"], task["Description"], task["Priority"])

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: The file '{file_path}' was not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Error: Failed to decode JSON. The file '{file_path}' is not in valid JSON format.")
        except KeyError as e:
            raise KeyError(f"Error: {e}. Ensure all tasks contain 'Title', 'Description', and 'Priority'.")
        except ValueError as e:
            raise ValueError(f"Error: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error: {e}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        # Convert list of Task objects into a list of dictionaries
        task_list = [task.to_dict() for task in self.tasks]

        # Use tabulate to format the output
        print(tabulate(task_list, headers="keys", tablefmt="fancy_grid"))

    def set_unsaved_changes_flag(self):
        self.unsaved_changes = True

    def reset_unsaved_changes_flag(self):
        self.unsaved_changes = False
