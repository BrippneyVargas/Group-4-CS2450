from fastapi import APIRouter
from model.task import Task

router = APIRouter()
tasks = []

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
@router.post("/tasks")
async def add_tasks(task: Task):
    tasks.append(task)
    return {"message": "task has been added"}

