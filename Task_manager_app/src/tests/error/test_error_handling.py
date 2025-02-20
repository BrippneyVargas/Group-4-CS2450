from Task_manager_app.src.model.task_manager import TaskManager
from io import StringIO
import unittest
import json
import sys
import os

# USE THE FOLLOWING TO RUN ALL TESTS: python -m unittest discover Task_manager_app/src/tests/error


class TaskCLIErrorTests(unittest.TestCase):
    def test_delete_nonexistent_task(self):
        tm = TaskManager()
        # t = Task("The Void", "This task does not exist in the TaskManager object.", 1)
        # ^^^ Sorry! I changed how the functionality works because it was simpler to do it another way

        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout

        t = "The Void"
        tm.delete_task(t)  # Run the function and capture the output

        sys.stdout = sys.__stdout__  # Reset stdout

        expected_output = "Task not found.\n"

        # Compare actual vs expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_load_malformed_json(self):
        self.test_dir = os.path.dirname(os.path.abspath(__file__))  # Get current test file's directory
        self.test_file = os.path.join(self.test_dir, "broken.json")

        tm = TaskManager()

        self.assertRaises(json.JSONDecodeError, tm.load_tasks(self.test_file))

    def test_invalid_priority(self):
        tm = TaskManager()

        self.assertRaises(ValueError, tm.add_task("Wrong Priority", "This priority should not exist.", -1))
        self.assertRaises(ValueError, tm.add_task("Wrong Priority", "This priority should not exist.", 4))

        assert tm.tasks == []
        # Check stderr for the right error message.


if __name__ == "__main__":
    unittest.main()
