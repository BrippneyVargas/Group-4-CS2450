#controller/tasks.py
from fastapi import APIRouter
from model.task import Task, AddTask


router = APIRouter()
tasks = []
task_id_counter= 1


@router.get("/")
async def root():
    return {"message": "Root of the app"}

# load all tasks
@router.get("/tasks")
async def get_tasks():
    return {"tasks": tasks}

# get a task by id
@router.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return {"task": task}
    return {"message": "task not found"}


# delete a task
@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "task has been deleted"}
    return {"message": "task not found"}


# add a task 
@router.post("/tasks", response_model=AddTask)
async def add_task(task: Task):
    '''Add a new task

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
    global task_id_counter
    new_task = AddTask(id=task_id_counter, title=task.title, description=task.description, priority=task.priority, tag=task.tag)
    tasks.append(new_task)
    task_id_counter += 1
    return new_task


# update a task
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
            task_updated= AddTask(
                id= task_id,
                title= updated_task.title,
                description= updated_task.description,
                priority= updated_task.priority,
                tag= updated_task.tag
            )
            tasks[index]= task_updated
            return task_updated