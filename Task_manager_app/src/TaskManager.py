from DatabaseManager import *
from fastapi import APIRouter
import requests

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