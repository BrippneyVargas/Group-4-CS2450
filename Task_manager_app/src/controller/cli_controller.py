
import argparse
import json
import os

TASKS_FILE = "tasks.json"

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": description})
    save_tasks(tasks)
    print(f"Task added: {description}")

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    print(f"Tasks Loaded")
    return []

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved to JSON.")

# Setup CLI
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # Delete task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="Task ID")

    # Save tasks
    subparsers.add_parser("save", help="Save tasks to JSON")

    args = parser.parse_args()

    # Handle commands
    if args.command == "add":
        add_task(args.description)
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "save":
        save_tasks(load_tasks())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
