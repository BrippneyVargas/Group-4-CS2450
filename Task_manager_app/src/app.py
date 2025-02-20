from model.task_manager import TaskManager


def add_new_task(mgr: TaskManager):
    task_title = input("Please enter the new task name: ")
    task_description = input("Please enter the new task's description: ")
    task_priority = input("Please enter the tasks priority (1-3, 1 being the highest priority and 3 being the lowest).")

    mgr.add_task(task_title, task_description, int(task_priority))
    mgr.set_unsaved_changes_flag()  # Make sure to note that there are unsaved changes.

    print("Task successfully created!")


def delete_task(mgr: TaskManager):
    task_title = input("Please enter the task title you would like to delete (please note that it must be exact): ")

    mgr.delete_task(task_title)
    mgr.set_unsaved_changes_flag()  # Make sure to note that there are unsaved changes.

    print("Task successfully deleted!")


def view_tasks(mgr: TaskManager):
    mgr.view_tasks()


def save_tasks(mgr: TaskManager):
    print("Saving tasks to tasks.json in root...")
    mgr.save_tasks("tasks.json")
    mgr.reset_unsaved_changes_flag()  # Once changes are saved make sure to note that there are not unsaved changes
    print("Tasks successfully saved!")


def load_tasks(mgr: TaskManager):
    print("Loading tasks from tasks.json...")
    mgr.load_tasks("tasks.json")
    print("Tasks loaded!")
    view_tasks()


def quit(mgr: TaskManager) -> bool:
    if mgr.unsaved_changes is True:
        print("You have changes that are unsaved! Would you like to save them now?")
        choice = input("Please enter 'y' or 'n', or 'q' to go back to the menu: ")
        if choice == "y":
            save_tasks(mgr)
        elif choice == "n":
            pass
        elif choice == "q":
            return True  # Go back to the menu
        else:
            print("Your input is not recognized.")
            quit(mgr)  # Send them back through.
        return False


def display_menu():
    print("Please select an option from the menu:\n")
    print("a - Add new task")
    print("d - Delete task")
    print("v - View all tasks")
    print("s - Save tasks")
    print("l - Load tasks")
    print("q - Quit program")


def handle_choice(mgr) -> bool:
    choice = input("Select your option: ")

    if choice == "a":
        add_new_task(mgr)
    elif choice == "d":
        delete_task(mgr)
    elif choice == "v":
        view_tasks(mgr)
    elif choice == "s":
        save_tasks(mgr)
    elif choice == "l":
        load_tasks(mgr)
    elif choice == "q":
        return quit(mgr)  # This will either return True or False, if it returns False it will end the while loop
    else:
        print("The selected option you inputted is not recognized. Please select a valid option.")
    return True


def main():
    print("Welcome to the Task Manager!")
    manager = TaskManager()
    continue_program = True

    while continue_program:
        display_menu()
        continue_program = handle_choice(manager)


if __name__ == "__main__":
    main()

