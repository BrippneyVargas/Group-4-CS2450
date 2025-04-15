from Task_manager_app.src.model.task_manager import TaskManager
from tabulate import tabulate
from io import StringIO
import unittest
import json
import sys

# USE THE FOLLOWING TO RUN ALL TESTS: python -m unittest discover Task_manager_app/src/tests/unit


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
        tm.delete_task("Get milk")

        assert tm.tasks == []

    def test_save_task(self):  # Rewrite this this isn't going to work.
        tm = TaskManager()
        tm.add_task("Get milk", "Go to Wal-mart and use your coupon", 2)
        tm.add_task("Walk the dog", "It's your turn and you know it", 1)
        tm.save_tasks("tests.json")

        file = open("tests.json", "r")
        data = json.load(file)
        file.close()

        assert data[0]["Title"] == "Get milk"
        assert data[0]["Description"] == "Go to Wal-mart and use your coupon"
        assert data[0]["Priority"] == 2

    def test_load_tasks(self):  # Rewrite this this isn't going to work.
        # shutil.copy("tests.json", ".")
        # new_path = os.path.join(".", "tasks.json")
        # shutil.move(os.path.join(".", "tests.json"), new_path)

        tm = TaskManager()

        tm.add_task("Get soda", "Use coupons at Smith's", 2)
        tm.add_task("Take medicine", "Should be underneath sink", 3)
        tm.save_tasks("tests.json")

        tm2 = TaskManager()
        tm2.load_tasks("tests.json")

        assert tm2.tasks[0].title == "Get soda"
        assert tm2.tasks[0].desc == "Use coupons at Smith's"
        assert tm2.tasks[0].priority == 2

        assert tm2.tasks[1].title == "Take medicine"
        assert tm2.tasks[1].desc == "Should be underneath sink"
        assert tm2.tasks[1].priority == 3

    def test_view_tasks(self):
        # Expected sorted task output in tabulate format
        expected_tasks = [
            {"Title": "Complete Project", "Description": "Finish the project report by...", "Priority": 1},
            {"Title": "Workout", "Description": "Exercise for 30 minutes at the gym.", "Priority": 2},
            {"Title": "Buy Groceries", "Description": "Get milk, eggs, and bread.", "Priority": 3},
        ]
        tm = TaskManager()

        for task in expected_tasks:
            tm.add_task(task["Title"], task["Description"], task["Priority"])

        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout

        tm.view_tasks()  # Run the function

        sys.stdout = sys.__stdout__  # Reset stdout

        expected_output = tabulate(expected_tasks, headers="keys", tablefmt="fancy_grid") + "\n"

        # Compare actual vs expected output
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()