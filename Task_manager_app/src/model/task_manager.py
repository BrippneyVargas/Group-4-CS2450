#model/task_manager.py
from typing import List, Literal
from tabulate import tabulate
from .task import Task
import json


class TaskManager:
    def __init__(self):
        """
        Initializes a new TaskManager object.

        Preconditions:
            - A TaskManager is not currently initialized.

        Known Issues:
            - None currently.
        """
        self.tasks: List[Task] = []
        self.unsaved_changes: bool = False

    def add_task(self, title: str, desc: str, priority: Literal[1, 2, 3]) -> None:
        """
        Creates a new task and adds it to the list of tasks

        Preconditions:
            - title is unique.
            - priority is 1, 2, or 3.

        Postconditions:
            - The size of self.tasks is larger by 1.

        Exceptions:
            - Raises ValueError if priority is not 1, 2, or 3.

        Known Issues:
            - None currently.

        Parameters:
            - title: str, the title of the task. This should be unique!
            - desc: str, a brief description of the task.
            - priority: int, a number expressing the priority of the task. Higher numbers are higher priority.
        """
        if priority not in [1, 2, 3]:
            raise ValueError("Priority must be 1, 2, or 3")
        self.tasks.append(Task(title, desc, priority))
        return

    def delete_task(self, task_title_to_delete: str) -> None:
        """
        Removes a task from the task list by the task name.

        Postconditions:
            - The size of self.tasks is smaller than one, or else the message "Task not found." is printed.

        Known Issues:
            - None currently.

        Parameters:
            - task_title_to_delete: str, the task you want to remove.
        """
        for i, task in enumerate(self.tasks):
            if task_title_to_delete == task.title:
                del self.tasks[i]
                break
        print("Task not found.")  # If the task is not found it will reach this and print to warn the user.

    def save_tasks(self, file_path: str) -> None:
        """
        Saves tasks to the json file found at file_path.

        Preconditions:
            - file_path leads to a json file.

        Postconditions:
            - file_path still leads to a json file.

        Known Issues:
            - Known currently.

        Parameters:
            - file_path: str, is the path to the file being written to, should be a JSON file.
        """
        task_data = [task.to_dict() for task in self.tasks]
        with open(file_path, "w") as f:
            json.dump(task_data, f, indent=4)

    def load_tasks(self, file_path: str) -> None:
        """
        Loads tasks from a JSON file with error handling.

        Preconditions:
            - file_path leads to a JSON file.

        Postconditions:
            - file_path still leads to a JSON file.

        Exceptions:
            - Raises FileNotFoundError if file_path does not exist.
            - Raises json.JSONDecodeError if the file is not a properly formatted JSON file.
            - Raises KeyError if the proper keys are not in every task in the JSON file.
            - Raises ValueError if a list is not obtained from json.load(f).

        Known Issues:
            - None currently.

        Parameters:
            - file_path: str, the file being read from, should be a JSON file.
        """
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

    def view_tasks(self) -> None:
        """
        Displays any tasks that are already saved.

        Known Issues:
            - None currently.
        """
        if not self.tasks:
            print("No tasks available.")
            return

        # Convert list of Task objects into a list of dictionaries
        task_list = [task.to_dict() for task in self.tasks]

        # Use tabulate to format the output
        print(tabulate(task_list, headers="keys", tablefmt="fancy_grid"))

    def set_unsaved_changes_flag(self):
        """
        Set self.unsaved_changes to True.

        Known Issues:
            - None currently.
        """
        self.unsaved_changes = True

    def reset_unsaved_changes_flag(self):
        """
        Set self.unsaved_changes to False.

        Known Issues:
            - None currently.
        """
        self.unsaved_changes = False