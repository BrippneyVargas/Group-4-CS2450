from fastapi import APIRouter, HTTPException
from model.Task import Task, TaskManager
from .SQLiteManager import SQLiteManager

class TaskController:
    def __init__(self):
        self.router = APIRouter()
        self.DB_PATH = "./Task_manager_app/src/model/tasks.db"
        self.sql_manager = SQLiteManager(self.DB_PATH)
        self.task_manager = TaskManager(self.sql_manager)
        self.task_manager.load_tasks()

        # Define routes
        self.router.add_api_route("/", self.root, methods=["GET"])
        self.router.add_api_route("/tasks", self.get_tasks, methods=["GET"])
        self.router.add_api_route("/tasks/{task_id}", self.get_task, methods=["GET"])
        self.router.add_api_route("/tasks/{task_id}", self.delete_task, methods=["DELETE"])
        self.router.add_api_route("/tasks", self.add_task, methods=["POST"])
        self.router.add_api_route("/tasks/{task_id}", self.update_task, methods=["PUT"])

    async def root(self):
        """Root of the backend application"""
        return {"message": "Root of the app"}

    async def get_tasks(self):
        """Get all tasks"""
        return {"tasks": [task.to_dict() for task in self.task_manager.task_list]}

    async def get_task(self, task_id: int):
        """Get a task by id"""
        for task in self.task_manager.task_list:
            if task.id == task_id:
                return {"task": task.__dict__}
        raise HTTPException(status_code=404, detail="Task not found")

    async def delete_task(self, task_id: int):
        """Delete a task by id"""
        for index, task in enumerate(self.task_manager.task_list):
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
                self.task_manager.task_list[index] = task_updated
                self.task_manager.save_tasks()
                self.task_manager.load_tasks()
                return {"message": "task has been deleted"}, 204
        raise HTTPException(status_code=404, detail="Task not found")

    async def add_task(self, task: Task):
        """Add a new task to the task list"""
        new_task = Task(
            id=None,
            title=task.title,
            description=task.description,
            priority=task.priority,
            tag=task.tag,
            active=task.active,
            completed=task.completed,
        )

        for task in self.task_manager.task_list:
            if task.title == new_task.title:
                raise HTTPException(status_code=409, detail="Duplicate task title")

        self.task_manager.add_task(new_task)
        self.task_manager.save_tasks()
        return new_task

    async def update_task(self, task_id: int, updated_task: Task):
        """Update the existing task"""
        for index, task in enumerate(self.task_manager.task_list):
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
                self.task_manager.task_list[index] = task_updated
                self.task_manager.save_tasks()
                return task_updated
        raise HTTPException(status_code=404, detail="Task not found")
    

DB_PATH = "./Task_manager_app/src/model/tasks.db"
sql_manager = SQLiteManager(DB_PATH)
task_manager = TaskManager(sql_manager)
task_manager.load_tasks()
task_controller = TaskController()
router = task_controller.router