from src.model.task_manager import TaskManager


def add_new_task(mgr: TaskManager):
    task_title = input("Please enter the new task name: ")
    task_description = input("Please enter the new task's description: ")
    task_priority = input("Please enter the tasks priority (enter a number; lower numbers are higher priority).")

    mgr.add_task(task_title, task_description, int(task_priority))
    mgr.set_unsaved_changes_flag()  # Make sure to note that there are unsaved changes.

    print("Task successfully created!")


def delete_task(mgr: TaskManager):
    task_title = input("Please enter the task title you would like to delete (please note that it must be exact): ")

    mgr.delete_task()


def display_menu():
    print("Please select an option from the menu:\n")
    print("a - Add new task")
    print("d - Delete task")
    print("v - View all tasks")
    print("s - Save tasks")
    print("l - Load tasks")
    print("q - Quit program")


def handle_choice(mgr):
    choice = input("Select your option: ")

    if choice == "a":
        add_new_task(mgr)
    elif choice == "d":
        pass
    elif choice == "v":
        pass
    elif choice == "s":
        pass
    elif choice == "l":
        pass
    elif choice == "q":
        pass
    else:
        print("The selected option you inputted is not recognized. Please select a valid option.")


def main():
    print("Welcome to the Task Manager!")
    manager = TaskManager()

    display_menu()
    handle_choice(manager)
