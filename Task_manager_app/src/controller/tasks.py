from fastapi import APIRouter
from model.Task import Task, TaskManager
from fastapi import HTTPException
from .SQLiteManager import SQLiteManager


router = APIRouter()
DB_PATH = "./Task_manager_app/src/model/tasks.db"
sql_manager = SQLiteManager(DB_PATH)
task_manager = TaskManager(sql_manager)

task_manager.load_tasks()


@router.get("/")
async def root():
    """Root of the backend application
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
    """Get all tasks
    Endpoint to retrieve all tasks.
    Param:
        - None

    Precondition:
        - None

    Postcondition:
        - Returns a list of all tasks

    Returns:
        dictionary object: An object containing all of tasks.
    """
    return {"tasks": [task.to_dict() for task in task_manager.task_list]}


@router.get("/tasks/{task_id}")
async def get_task(task_id: int):
    """Get a task by id
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

    for task in task_manager.task_list:
        if task.id == task_id:
            return {"task": task.__dict__}
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task by id
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

    for index, task in enumerate(task_manager.task_list):
        if task.id == task_id:
            removed_task = task
            task_updated = Task(
                id=task_id,
                title=removed_task.title,
                description=removed_task.description,
                priority=removed_task.priority,
                tag=removed_task.tag,
                active=False,
                completed=removed_task.completed,
            )
            task_manager.task_list[index] = task_updated
            task_manager.save_tasks()
            task_manager.load_tasks()
            return {"message": "task has been deleted"}, 204
    # for task in task_manager.task_list:
    #     if task.id == task_id:
    #         task_manager.task_list.remove(task)
    #         task_manager.save_tasks()
    #         return {"message": "task has been deleted"}, 204
    # raise HTTPException(status_code=404, detail="Task not found")


@router.post("/tasks")
async def add_task(task: Task):
    """Add a new task to the task list
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
    """
    # global task_id_counter
    new_task = Task(
        id=None,
        title=task.title,
        description=task.description,
        priority=task.priority,
        tag=task.tag,
        active=task.active,
        completed=task.completed,
    )

    for task in task_manager.task_list:
        if task.title == new_task.title:
            raise HTTPException(status_code=409, detail="Duplicate task title")


    task_manager.add_task(new_task)
    task_manager.save_tasks()
    return new_task


@router.put("/tasks/{task_id}")
async def update_task(task_id: int, updated_task: Task):
    """Update the existing task
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
    """
    for index, task in enumerate(task_manager.task_list):
        if task.id == task_id:
            task_updated = Task(
                id=task_id,
                title=updated_task.title,
                description=updated_task.description,
                priority=updated_task.priority,
                tag=updated_task.tag,
                active=updated_task.active,
                completed=updated_task.completed,
            )
            task_manager.task_list[index] = task_updated
            task_manager.save_tasks()
            return task_updated
