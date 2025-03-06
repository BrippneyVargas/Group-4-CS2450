from fastapi import FastAPI
from model.task import Task
app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Root of the app"}

tasks = []

# load all tasks
@app.get("/tasks")
async def get_tasks():
    return {"tasks": tasks}

# get a task by id
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return {"task": task}
    return {"message": "task not found"}

# delete a task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "task has been deleted"}
    return {"message": "task not found"}

# add a task
@app.post("/tasks")
async def add_tasks(task: Task):
    tasks.append(task)
    return {"message": "task has been added"}

