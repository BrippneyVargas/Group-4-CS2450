from DatabaseManager import *
import json
import os
from Task import *

class JSONManager(DatabaseManager):
    def __init__(self, json_path: str) -> None:
        self.__json_path = json_path

        self.load_all()

    def load_all(self) -> None:
        """
        Load tasks from a JSON file.
        This function reads tasks from a JSON file specified by the global variable TASKS_FILE.
        It updates the global variables 'tasks' and 'task_id_counter' with the data from the file.
        Each task in the JSON file is converted into an AddTask object.
        """
        if os.path.exists(self.__json_path):
            with open(self.__json_path, "r") as file:
                data = json.load(file)
                self.__tasks = [Task(**task) for task in data["tasks"]]
                self.__task_id_counter = data["task_id_counter"]

    def save_all(self) -> None:
        """
        Saves the current list of tasks and the task ID counter to a file.
        This function serializes the tasks and task ID counter into a JSON format
        and writes them to the file specified by TASKS_FILE.
        Raises:
            IOError: If there is an issue writing to the file.
        """
        with open(self.__json_path, "w") as file:
            data = {
                "tasks": [task.__dict__ for task in self.__tasks],
                "task_id_counter": self.__task_id_counter
            }
            json.dump(data, file, indent=4)
