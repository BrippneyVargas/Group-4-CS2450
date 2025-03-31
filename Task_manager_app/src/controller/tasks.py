from fastapi import APIRouter
from Task import Task, AddTask
import json
import os
from fastapi import HTTPException

tasks = []
task_id_counter = 1
TASKS_FILE = "./Task_manager_app/src/data/tasks.json"
router = APIRouter()



def load_tasks():
    """
    Load tasks from a JSON file.
    This function reads tasks from a JSON file specified by the global variable TASKS_FILE.
    It updates the global variables 'tasks' and 'task_id_counter' with the data from the file.
    Each task in the JSON file is converted into an AddTask object.
    """
    # global tasks, task_id_counter
    # if os.path.exists(TASKS_FILE):
    #     with open(TASKS_FILE, "r") as file:
    #         data = json.load(file)
    #         # If any task doesn't have an 'id', assign it a default value
    #         for task in data["tasks"]:
    #             if "id" not in task:  # If the task doesn't have an id, assign one
    #                 task["id"] = task_id_counter
    #             task_id_counter = max(task_id_counter, task["id"] + 1)  # Update task_id_counter accordingly
    #         tasks = [AddTask(**task) for task in data["tasks"]]
    #         print(f"Loaded {len(tasks)} tasks from file.")
    global tasks, task_id_counter
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            data = json.load(file)
            tasks = [AddTask(**task) for task in data["tasks"]]  # This ensures AddTask objects are used
            task_id_counter = data["task_id_counter"]


def save_tasks():
    """
    Saves the current list of tasks and the task ID counter to a file.
    This function serializes the tasks and task ID counter into a JSON format
    and writes them to the file specified by TASKS_FILE.
    Raises:
        IOError: If there is an issue writing to the file.
    """
    with open(TASKS_FILE, "w") as file:
        data = {
            "tasks": [task.to_dict() for task in tasks],
            "task_id_counter": task_id_counter
        }
        json.dump(data, file, indent=4)


load_tasks()


@router.get("/")
async def root():
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


@router.get("/tasks")
async def get_tasks():
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
    # return {"tasks": tasks}
    return {"tasks": [task.__dict__ for task in tasks]} 



@router.get("/tasks/{task_id}")
async def get_task(task_id: int):
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

    for task in tasks:
        if task.id == task_id:
            return {"task": task.__dict__}
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
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

    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            save_tasks()
            return {"message": "task has been deleted"}, 204
    raise HTTPException(status_code=404, detail="Task not found")


@router.post("/tasks", response_model=AddTask)
async def add_task(task: Task):  # Use Task for input, AddTask for output
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
    print("@router add_task():", task.dict())  # Print the incoming Task object
    global task_id_counter
    new_task = AddTask(id=task_id_counter, title=task.title, description=task.description, priority=task.priority, tag=task.tag)
    
    print("@router new_task:", new_task.dict())  # Print the AddTask object after assigning id
    
    tasks.append(new_task)
    task_id_counter += 1
    save_tasks()
    return new_task



@router.put("/tasks/{task_id}", response_model=AddTask)
async def update_task(task_id: int, updated_task: Task):
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
    for index, task in enumerate(tasks):
        if task.id == task_id:
            task_updated = AddTask(
                id=task_id,
                title=updated_task.title,
                description=updated_task.description,
                priority=updated_task.priority,
                tag=updated_task.tag
            )
            tasks[index] = task_updated
            return task_updated