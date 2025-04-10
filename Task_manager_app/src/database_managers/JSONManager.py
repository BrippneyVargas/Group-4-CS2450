from database_managers.DatabaseManager import DatabaseManager
from fastapi import APIRouter, HTTPException
from model.Task import Task
from typing import Any, override
import json
import os

router = APIRouter()

class JSONManager(DatabaseManager):
    def __init__(self, file_path):
        self.__id_counter = 1
        self.__tasks = []
        self.__tasks_file = file_path

        self.load_all()

    @override
    def load_all(self) -> None:
        """
        Load tasks from a JSON file.
        This function reads tasks from a JSON file specified by the global variable TASKS_FILE.
        It updates the global variables 'tasks' and 'task_id_counter' with the data from the file.
        Each task in the JSON file is converted into an AddTask object.
        """    
        if os.path.exists(self.__tasks_file):
            try:
                with open(self.__tasks_file, "r") as file:
                    data = json.load(file)
                    self.__tasks = [Task(**task) for task in data.get("tasks", [])]
                    self.__id_counter = data.get("task_id_counter", 1)
            except (json.JSONDecodeError, KeyError): # Where JSON is empty or invalid.
                self.__tasks = []
                self.__id_counter = 1
                
    @override
    def save_all(self) -> None:
        """
        Saves the current list of tasks and the task ID counter to a file.
        This function serializes the tasks and task ID counter into a JSON format
        and writes them to the file specified by TASKS_FILE.
        Raises:
            IOError: If there is an issue writing to the file.
        """
        with open(self.__tasks_file, "w") as file:
            data = {
                "tasks": [task.to_dict() for task in self.__tasks],
                "task_id_counter": self.__id_counter
            }
            json.dump(data, file, indent=4)

    @override
    @router.get("/")
    async def root(self) -> dict:
        """ Root of the backend application
        Root endpoint of the application.
        Param:
            - None

        Precondition:
            - None

        Postcondition:
            - Returns a welcome message

        Returns:
            json object (Dictionary turns into JSON): An object containing a welcome message.
        """
        return {"message": "Root of the app"}

    @override
    @router.get("/tasks")
    async def get_all(self) -> dict:
        """ Get all tasks
        Endpoint to retrieve all tasks.
        Param:
            - None

        Precondition:
            - None

        Postcondition:
            - Returns a list of all tasks

        Returns:
            json object: An object containing all of tasks.
        """
        return {"tasks": [task.__dict__ for task in self.__tasks]}

    @override
    @router.get("/tasks/{task_id}")
    async def get(self, primary_key: int) -> dict:
        """ Get a task by id
        Retrieve a task by its id.
        Param:
            - task_id (int): The id of the task to retrieve.

        Precondition:
            - task_id must be a valid integer.
            - The task with the given task_id should exist in the tasks list.

        Postcondition:
            - If the task with the given task_id exists, it is returned.
            - If the task with the given task_id does not exist, a message indicating that the task was not found is returned.

        Returns:
            json object: An object containing the task if found, or a message indicating that the task was not found.
        """
        for task in self.__tasks:
            if task.id == primary_key:
                return {"task": task.__dict__}
        raise HTTPException(status_code=404, detail="Task not found")

    @override
    @router.delete("/tasks/{task_id}")
    async def delete(self, primary_key: int) -> dict:
        """ Delete a task by id
        Deletes a task with the given task_id from the tasks list.
        Param:
            - task_id (int): The id of the task to delete.

        Precondition:
            - task_id must be a valid integer.
            - The task with the given task_id should exist in the tasks list.

        Postcondition:
            - If the task with the given task_id exists, it is removed from the tasks list.
            - If the task with the given task_id does not exist, a message indicating that the task was not found is returned.
        Args:
            task_id (int): The ID of the task to be deleted.
        Returns:
            json object: An object containing a message indicating whether the task was successfully deleted or not.
        """
        for task in self.__tasks:
            if task.id == primary_key:
                self.__tasks.remove(task)
                self.save_all()
                return {"message": "task has been deleted"}, 204
        raise HTTPException(status_code=404, detail="Task not found")

    @override
    @router.post("/tasks")
    async def add(self, item_to_add: Any) -> Any:
        '''Add a new task to the task list
        The add_task() function accepts a user input (a task object), auto increments the id, and append the object to the task list.

        Param:
            - "task: Task" is the request body in the POST request. It includes details of the Task object such as:
                - title: str - title of the task
                - description: str - description of the task
                - priority: int - level of priority (1:high, 2:medium, 3:low)
                - tag: str - A tag to categorize the task

        Precondition:
            - Valid task object with title, description, priority, and tag
            - global task_id_counter has been properly initialized
            - task list has been initialized to store the task objects (initialize an empty list)

        Postcondition:
            - A new task object is created with an auto-incremented ID, title, description, priority, and tag
            - The new task object is appended to the task list
            - The global task_id_counter is incremented by 1 for the next task

        Returns:
            - new_task: The new task object

        Exceptions:
            - None (yet)
        '''
        print("@router add_task():", item_to_add.dict())
        new_task = Task(id=self.__id_counter, title=item_to_add.title, description=item_to_add.description, priority=item_to_add.priority, tag=item_to_add.tag)
        
        print("@router new_task:", new_task.dict())  
        
        self.__tasks.append(new_task)
        self.__id_counter += 1
        self.save_tasks()
        return new_task

    @override
    @router.put("/tasks/{task_id}")
    async def update(self, primary_key: Any, updated_item: Any) -> dict:
        '''Update the existing task
            The update_task() function accepts a user input (a task object) on the task that is already in the task list, using task_id as a reference or identifier.

        Param:
            - task_id: int - is useed to identify the task to be updated
            - updated_task: Task - updating the task object with new details. The tasks object include title, description, priority, and tag

        Precondition:
            - Valid task object with title, description, priority, and tag
            - task_id must match the task object in the task list

        Postcondition:
            - The existing task is updated and append to the task list

        Returns:
            - task_updatedTask: task object with updated details

        Exceptions:
            - None (yet)
        '''
        for index, task in enumerate(self.__tasks):
            if task.id == primary_key:
                task_updated = Task(
                    id=primary_key,
                    title=updated_item.title,
                    description=updated_item.description,
                    priority=updated_item.priority,
                    tag=updated_item.tag
                )
                self.__tasks[index] = task_updated
                self.save_tasks()
                return task_updated
