from DatabaseManager import *
import requests
import streamlit as st
from Task import *

class JSONManager(DatabaseManager):
    def __init__(self, json_path: str) -> None:
        self.__json_path = json_path
        
        self.load_all()

    def load_all(self) -> None:
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
            return response.json().get("tasks", [])
        except requests.RequestException as e:
            st.error(f"Error fetching tasks: {e}")

    def save_all(self) -> None:
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
