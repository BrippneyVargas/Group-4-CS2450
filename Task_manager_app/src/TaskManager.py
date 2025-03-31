"""
Task Manager Streamlit Application

This Streamlit application provides a user interface for managing tasks with a FastAPI backend.
The application allows users to create, view, edit, and delete tasks with features such as
priority levels, tags, and pagination.

Classes:
    TaskColor: Defines color constants used for styling the application.
    TaskStyler: Applies custom CSS styling to the Streamlit application.
    TaskManager: Handles communication with the FastAPI backend for CRUD operations.
        - fetch_tasks: Retrieves tasks from the backend API
        - save_task: Sends a new task to the backend for storage
        - update_task: Modifies an existing task in the backend
        - delete_task: Removes a task from the backend
        - load_tasks: Loads tasks from the API by calling fetch_tasks
    TaskUI: Manages the user interface components and interactions.
        - Provides forms for adding and editing tasks
        - Displays tasks with pagination support
        - Handles session state for editing tasks and pagination

Usage:
    Run this application with Streamlit:
        $ streamlit run app.py

    Note: Requires a FastAPI backend running on http://localhost:8000/tasks

Dependencies:
    - streamlit
    - requests
    - os
    - sys

Author: Group 4
Copyright: Task Manager © 2025
"""

from DatabaseManager import DatabaseManager
from JSONManager import JSONManager
from SQLiteManager import *
from fastapi import APIRouter, HTTPException
from controller import router
import os
import requests
import streamlit as st
from Styler import Styler
import sys
from Task import Task
from UI import UI


class TaskManager:
    """Manage tasks using the FastAPI backend."""

    API_URL = "http://localhost:8000/tasks"  # Make sure FastAPI is running on this URL

    def __init__(self, db_manager: DatabaseManager, router: APIRouter):
        self.db_manager = db_manager
        self.tasks = []

        self.db_manager.load_all() #load tasks from database 
        # self.load_tasks()

    def fetch_tasks(self):
        """Fetch a task from the backend via FastAPI."""
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            self.tasks = [Task(**task) for task in response.json().get("tasks", [])]
        except requests.RequestException as e:
            st.error(f"Error fetching tasks: {e}")


    def save_task(self, task):
        """Save a task to the backend via FastAPI."""
        with st.spinner("Saving task..."):
            try:
                task_dict = task.to_dict() if hasattr(task, "to_dict") else task  # Convert Task object to dict               
                response = requests.post(self.API_URL, json=task_dict)
                response.raise_for_status()
                # st.success("Task saved successfully!")
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
                # st.markdown("<p style='background-color: rgba(60, 179, 113, 0.5); padding: 10px;'>Tasks loaded successfully!</p>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Unexpected error while loading tasks: {e}")


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(current_dir)

    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    
    if st.button("Switch Theme"):
        st.session_state.dark_mode = not st.session_state.dark_mode

    Styler.apply_custom_theme(st.session_state.dark_mode)

    db_manager = JSONManager(TaskManager.API_URL, "data/test.json")
    task_manager = TaskManager(db_manager, router)
    task_ui = UI(task_manager)  # Initialize UI
    task_ui.initialize_session_state()  # Initialize session state
    task_ui.run()  # Run the UI

if __name__ == "__main__":
    main()
