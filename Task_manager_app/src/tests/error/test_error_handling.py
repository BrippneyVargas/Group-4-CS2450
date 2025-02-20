from src.model.task_manager import TaskManager
from src.model.task
import unittest
import shutil
import json
import os

# USE THE FOLLOWING TO RUN ALL TESTS: python -m unittest discover src/tests/error


class TaskCLIErrorTests(unittest.TestCase):
    def test_delete_nonexistent_task(self):
        tm = TaskManager()
        t = Task("The Void", "This task does not exist in the TaskManager object.", 1)
        tm.delete_task(t)
        # Check stderr for the right error message.

    def test_load_malformed_json(self):
        shutil.copy("test.json", ".")
        new_path = os.path.join(".", "tasks.json")
        shutil.move(os.path.join(".", "test.json"), new_path)

        tm = TaskManager()
        # Check stderr for the right error message.

    def test_invalid_priority(self):
        tm = TaskManager()

        tm.add_task("Wrong Priority", "This priority should not exist.", -1)
        tm.add_task("Wrong Priority", "This priority should not exist.", 4)

        assert tm.tasks == []
        # Check stderr for the right error message.

if __name__ == "__main__":
    unittest.main()
