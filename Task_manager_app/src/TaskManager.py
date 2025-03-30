from DatabaseManager import *
from fastapi import APIRouter
import requests
from Task import *

class TaskManager:
    """Manage tasks using the FastAPI backend."""

    API_URL = "http://localhost:8000/tasks"  # Make sure FastAPI is running on this URL

    def __init__(self, db_manager: DatabaseManager, router: API):
        self.__db_manager = db_manager
        self.tasks = []

        self.__db_manager.load_tasks()

    def fetch_tasks(self):
        """Load tasks from the FastAPI backend.

        Precondition:
            - streamlit is downloaded and imported.
            - FastAPI is installed
            - self.API_URL is a valid URL for the FastAPI backend.

        Postcondition:
            - If successful, list of task is fetched from the API and stored in self.tasks.
            - self.tasks remains an empty list if there is no task in the task list.

        Exceptions:
            - If there's an error fetching tasks, raise RequestException with the error message.

        Known issues:
            - If streamlit and FastAPI package is not installed, there'll be an error.
        """
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            self.tasks = response.json().get("tasks", [])
        except requests.RequestException as e:
            st.error(f"Error fetching tasks: {e}")

    def save_task(self, task):
        """Save a new task via FastAPI.
        The json file is saved as tasks.json under the src/data directory.

        Precondition:
            - streamlit is downloaded and imported.
            - FastAPI is installed
            - self.API_URL is a valid URL for the FastAPI backend.

        Postcondition:
            - The task added is successfully saved to a JSON file.

        Exceptions:
            - If there's an error saving task, raise RequestException with the error message.

        Known issues:
             If streamlit and FastAPI package is not installed, there'll be an error.
        """
        with st.spinner("Saving task..."):
            try:
                response = requests.post(self.API_URL, json=task)
                response.raise_for_status()
                st.success("Task saved successfully!")
            except requests.RequestException as e:
                st.error(f"Error saving task: {e}")

    def update_task(self, task_id, updated_task):
        """Update a task identified by task_id via FastAPI.

        Precondition:
            - streamlit is downloaded and imported.
            - FastAPI is installed
            - task_id is a valid task id and it matches the task already in the task list.

        Postcondition:
            - The task is successfully updated.

        Exceptions:
            - If there's an error updating the task, raise RequestException with the error message.

        Known issues:
            - "INFO: 127.0.0.1:46460 - "PUT /tasks/111 HTTP/1.1" 500 Internal Server Error" can show up and prevent task to be updated.
        """
        with st.spinner("Updating task..."):
            try:
                response = requests.put(f"{self.API_URL}/{task_id}", json=updated_task)
                response.raise_for_status()
                st.success("Task updated successfully!")
            except requests.RequestException as e:
                st.error(f"Error updating task: {e}")

    def delete_task(self, task_id):
        """Delete a task via FastAPI."""
        with st.spinner("Deleting task..."):
            try:
                response = requests.delete(f"{self.API_URL}/{task_id}")
                response.raise_for_status()
                st.markdown("<p style='background-color: #BDB76B; color: red;'>&nbsp;&nbsp;delete</p>", unsafe_allow_html=True)
            except requests.RequestException as e:
                st.error(f"Error deleting task: {e}")

    def load_tasks(self):
        """Load tasks from the API."""
        try:
            self.fetch_tasks()
            # if self.tasks:
            #     st.markdown("<p style='background-color: rgba(60, 179, 113, 0.5); padding: 10px;'>Tasks loaded successfully!</p>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Unexpected error while loading tasks: {e}")

    @router.get("/")
    async def root():
        """ Root of the backend application
        Root endpoint of the application.
        Param:
            - None

        Precondition:
            - None

        Postcondition:
            - Returns a welcome message

        Returns:
            json object (Dictionary turns into JSON): An object containing a welcome message.
        """
        return {"message": "Root of the app"}


    @router.get("/tasks")
    async def get_tasks(self):
        """ Get all tasks
        Endpoint to retrieve all tasks.
        Param:
            - None

        Precondition:
            - None

        Postcondition:
            - Returns a list of all tasks

        Returns:
            json object: An object containing all of tasks.
        """
        return {"tasks": self.__tasks}


    @router.get("/tasks/{task_id}")
    async def get_task(self, task_id: int):
        """ Get a task by id
        Retrieve a task by its id.
        Param:
            - task_id (int): The id of the task to retrieve.

        Precondition:
            - task_id must be a valid integer.
            - The task with the given task_id should exist in the tasks list.

        Postcondition:
            - If the task with the given task_id exists, it is returned.
            - If the task with the given task_id does not exist, a message indicating that the task was not found is returned.

        Returns:
            json object: An object containing the task if found, or a message indicating that the task was not found.
        """

        for task in self.__tasks:
            if task.task_id == task_id:
                return {"task": task}
        raise HTTPException(status_code=404, detail="Task not found")


    @router.delete("/tasks/{task_id}")
    async def delete_task(self, task_id: int):
        """ Delete a task by id
        Deletes a task with the given task_id from the tasks list.
        Param:
            - task_id (int): The id of the task to delete.

        Precondition:
            - task_id must be a valid integer.
            - The task with the given task_id should exist in the tasks list.

        Postcondition:
            - If the task with the given task_id exists, it is removed from the tasks list.
            - If the task with the given task_id does not exist, a message indicating that the task was not found is returned.
        Args:
            task_id (int): The ID of the task to be deleted.
        Returns:
            json object: An object containing a message indicating whether the task was successfully deleted or not.
        """

        for task in self.__tasks:
            if task.id == task_id:
                self.__tasks.remove(task)
                self.save_tasks()
                return {"message": "task has been deleted"}, 204
        raise HTTPException(status_code=404, detail="Task not found")


    @router.post("/tasks", response_model=Task)
    async def add_task(self, task: Task):
        print(task)
        '''Add a new task to the task list
        The add_task() function accepts a user input (a task object), auto increments the id, and append the object to the task list.

        Param:
            - "task: Task" is the request body in the POST request. It includes details of the Task object such as:
                - title: str - title of the task
                - description: str - description of the task
                - priority: int - level of priority (1:high, 2:medium, 3:low)
                - tag: str - A tag to categorize the task

        Precondition:
            - Valid task object with title, description, priority, and tag
            - global task_id_counter has been properly initialized
            - task list has been initialized to store the task objects (initialize an empty list)

        Postcondition:
            - A new task object is created with an auto-incremented ID, title, description, priority, and tag
            - The new task object is appended to the task list
            - The global task_id_counter is incremented by 1 for the next task

        Returns:
            - new_task: The new task object

        Exceptions:
            - None (yet)
        '''
        new_task = Task(task_id=self.__task_id_counter, title=task.title, description=task.description, priority=task.priority, tag=task.tag)
        tasks.append(new_task)
        self.__task_id_counter += 1
        self.save_tasks()
        return new_task


    @router.put("/tasks/{task_id}", response_model=Task)
    async def update_task(task_id: int, updated_task: Task):
        '''Update the existing task
            The update_task() function accepts a user input (a task object) on the task that is already in the task list, using task_id as a reference or identifier.

        Param:
            - task_id: int - is useed to identify the task to be updated
            - updated_task: Task - updating the task object with new details. The tasks object include title, description, priority, and tag

        Precondition:
            - Valid task object with title, description, priority, and tag
            - task_id must match the task object in the task list

        Postcondition:
            - The existing task is updated and append to the task list

        Returns:
            - task_updatedTask: task object with updated details

        Exceptions:
            - None (yet)
        '''
        for index, task in enumerate(tasks):
            if task.id == task_id:
                task_updated = Task(
                    id=task_id,
                    title=updated_task.title,
                    description=updated_task.description,
                    priority=updated_task.priority,
                    tag=updated_task.tag
                )
                tasks[index] = task_updated
                return task_updated