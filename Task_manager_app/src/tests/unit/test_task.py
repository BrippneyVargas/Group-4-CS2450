from src.model.task_manager import TaskManager
import unittest
import shutil
import json
import os

# USE THE FOLLOWING TO RUN ALL TESTS: python -m unittest discover src/tests/unit


class TaskCLITests(unittest.TestCase):
    def test_add_task(self):  # Passed: 2/19/25 by Jacob West
        tm = TaskManager()
        tm.add_task("Get milk", "Go to Wal-mart and use your coupon", 2)

        assert tm.tasks[0].title == "Get milk"
        assert tm.tasks[0].desc == "Go to Wal-mart and use your coupon"
        assert tm.tasks[0].priority == 2

    def test_delete_task(self):  # Passed: 2/19/25 by Jacob West
        tm = TaskManager()
        tm.add_task("Get milk", "Go to Wal-mart and use your coupon", 2)
        tm.delete_task(tm.tasks[0])

        assert tm.tasks == []

    def test_save_task(self):  # Rewrite this this isn't going to work.
        tm = TaskManager()
        tm.add_task("Get milk", "Go to Wal-mart and use your coupon", 2)
        tm.add_task("Walk the dog", "It's your turn and you know it", 1)
        tm.save_tasks()

        file = open("tasks.json", "r")
        data = json.load(file)
        file.close()

        assert data[0]["title"] == "Get milk"
        assert data[0]["desc"] == "Go to Wal-mart and use your coupon"
        assert data[0]["priority"] == 2

    def test_load_tasks(self):  # Rewrite this this isn't going to work.
        shutil.copy("test.json", ".")
        new_path = os.path.join(".", "tasks.json")
        shutil.move(os.path.join(".", "test.json"), new_path)

        tm = TaskManager()

        assert tm.tasks[0].title == "Get soda"
        assert tm.tasks[0].desc == "Use coupons at Smith's"
        assert tm.tasks[0].priority == 2

        assert tm.tasks[1].title == "Take medicine"
        assert tm.tasks[1].desc == "Should be underneath sink"
        assert tm.tasks[1].priority == 3


if __name__ == "__main__":
    unittest.main()
