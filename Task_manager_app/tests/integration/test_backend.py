import requests
import json
import unittest
import sys
import os
"""
Before running the test, make sure to run the backend server by executing main.py.

"""

BASE_URL = "http://127.0.0.1:8000"  # Update with your FastAPI server URL if different

class TestFastAPIServer(unittest.TestCase):
    def test_root_endpoint(self):
        response = requests.get(f"{BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_create_task(self):
        payload = {"title": "Test Task", "description": "This is a test task", "priority": 1, "tag": "test"}
        response = requests.post(f"{BASE_URL}/tasks", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())
        self.assertEqual(response.json()["title"], payload["title"])

    def test_get_task(self):
        # Create a task first
        payload = {"title": "Test Task", "description": "This is a test task", "priority": 1, "tag": "test"}
        create_response = requests.post(f"{BASE_URL}/tasks", json=payload)
        create_response_json = create_response.json()
        if "id" not in create_response_json:
            self.fail(f"Response JSON does not contain 'id': {create_response_json}")
        task_id = create_response_json["id"]

        # Fetch the created task
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["task"]["id"], task_id)

    def test_update_task(self):
        # Create a task first
        payload = {"title": "Test Task", "description": "This is a test task", "priority": 1, "tag": "test"}
        create_response = requests.post(f"{BASE_URL}/tasks", json=payload)
        task_id = create_response.json()["id"]

        # Update the task
        update_payload = {"title": "Test Task", "description": "This is a test task", "priority": 1, "tag": "test"}
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], update_payload["title"])

    def test_delete_task(self):
        # Create a task first
        payload = {"title": "Test Task", "description": "This is a test task", "priority": 1, "tag": "test"}
        create_response = requests.post(f"{BASE_URL}/tasks", json=payload)
        
        task_id = create_response.json()["id"]


        # Delete the task
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)

        # Verify the task is deleted
        get_response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        self.assertEqual(get_response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
