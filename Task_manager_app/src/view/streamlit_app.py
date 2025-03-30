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
import os
import sys

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

def main():
    """Main entry point for the Streamlit application."""
    task_manager = TaskManager()  # Initialize TaskManager communicating with FastAPI
    task_ui = TaskUI(task_manager)  # Initialize TaskUI
    task_ui.initialize_session_state()  # Initialize session state
    task_ui.run()  # Run the UI

if __name__ == "__main__":
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    
    if st.button("Switch Theme"):
        st.session_state.dark_mode = not st.session_state.dark_mode


    TaskStyler.apply_custom_theme(st.session_state.dark_mode)

    main()



