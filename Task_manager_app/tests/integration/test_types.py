from fastapi import APIRouter
from Task_manager_app.src.database_managers.JSONManager import *
import requests
from Task_manager_app.src.model.TaskManager import *
import unittest

BASE_URL = "http://127.0.0.1:8000"  # Update with your FastAPI server URL if different

class TestTaskManager(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.task_manager = TaskManager(JSONManager("http://localhost:8000/tasks", "data/test.json"), APIRouter())

    def test_save_task(self):
        self.assertRaises(TypeError, self.task_manager.save_task(12))

    def test_update_task(self):
        self.assertRaises(TypeError, self.task_manager.update_task("abc", 12))
