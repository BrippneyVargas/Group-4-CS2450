
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

import streamlit as st
import requests
import os
import sys

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)


class TaskColor:
    """Define colors for styling purposes."""
    BACKGROUND_DARK = '#121212'
    PRIMARY_LIGHT = '#7BDFF2'
    HIGH_PRIORITY = '#FF4136'
    MEDIUM_PRIORITY = '#FF851B'
    LOW_PRIORITY = '#FFDC00'


class TaskStyler:
    """Apply custom CSS styles for the application."""

    @staticmethod
    def apply_custom_theme():
        """
        Customize the Streamlit application with colors, theme and styles.

        Precondition:
                -  streamlit is downloaded and imported. 
            
        Postcondition:
            - The tasks are displayed in a table format.
            - If no tasks exist, a message is displayed as "No tasks to display."
        
        Known issues:
            - If streamlit package is not installed, there'll be an error: ModuleNotFoundError: No module named 'streamlit'
        
        """
        custom_css = f"""
        <style>
        body, .stApp {{ overflow: hidden !important; max-height: 100vh; }}
        .stApp {{ background-color: {TaskColor.BACKGROUND_DARK}; max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        ::-webkit-scrollbar {{ display: none; }}
        .priority-high {{ background-color: {TaskColor.HIGH_PRIORITY}; color: white; padding: 5px 10px; border-radius: 5px; text-align: center; }}
        .priority-medium {{ background-color: {TaskColor.MEDIUM_PRIORITY}; color: white; padding: 5px 10px; border-radius: 5px; text-align: center; }}
        .priority-low {{ background-color: {TaskColor.LOW_PRIORITY}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
        .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 20px 0; color: {TaskColor.PRIMARY_LIGHT}; font-size: 0.9em; background-color: {TaskColor.BACKGROUND_DARK}; }}
        .app-title {{ color: {TaskColor.PRIMARY_LIGHT}; text-align: center; font-size: 2.5em; margin-bottom: 20px; font-weight: bold; }}
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)


class TaskManager:
    """Manage tasks using the FastAPI backend."""

    API_URL = "http://localhost:8000/tasks"  # Make sure FastAPI is running on this URL

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def fetch_tasks(self):
        """Load tasks from the FastAPI backend.

        Precondition:
            - streamlit is downloaded and imported. 
            - FastAPI is installed 
            - self.API_URL is a valid URL for the FastAPI backend.
            
        Postcondition:
            - If successful, list of task is fetched from the API and stored in self.tasks. 
            - self.tasks remains an empty list of there is no task in the task list. 
        
        Exceptions:
            - If there's an error fetching tasks, raise RequestException with the error message.
        
        Known issues:
            - If streamlit and FastAPI package is not installed, there'll be an error.       
            
        """
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            self.tasks = response.json().get("tasks", [])
            # st.success("Tasks loaded successfully!")
        except requests.RequestException as e:
            st.error(f"Error fetching tasks: {e}")

    def save_task(self, task):
        """Save a new task via FastAPI.

        Precondition:
            - streamlit is downloaded and imported. 
            - FastAPI is installed 
            - self.API_URL is a valid URL for the FastAPI backend.
            
        Postcondition:
            - The tasks added is successfully saved to a json file. 
        
        Exceptions:
            - If there's an error fetching tasks, raise RequestException with the error message.
        
        Known issues:
             If streamlit and FastAPI package is not installed, there'll be an error.  
        """
        with st.spinner("Saving task..."):
            try:
                response = requests.post(self.API_URL, json=task)
                response.raise_for_status()
                st.success("Task added successfully!")
            except requests.RequestException as e:
                st.error(f"Error saving task: {e}")

    def update_task(self, task_id, updated_task):
        """Update a task identified by task_id via FastAPI.
        
        Precondition:
            - streamlit is downloaded and imported. 
            - FastAPI is installed 
            - task_id is a valid task id and it matches the task already in the task list 
            
        Postcondition:
            - The task is successfully updated. 
        
        Exceptions:
            - If there's an error fetching tasks, raise RequestException with the error message.
        
        Known issues:
            - "INFO: 127.0.0.1:46460 - "PUT /tasks/111 HTTP/1.1" 500 Internal Server Error" can show up and prevent task to be updated
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
                st.success("Task deleted successfully!")
            except requests.RequestException as e:
                st.error(f"Error deleting task: {e}")

    def load_tasks(self):
        """Load tasks from the API."""
        self.fetch_tasks()


class TaskUI:
    """Manage the user interface for the Task Manager."""

    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.initialize_session_state()
        TaskStyler.apply_custom_theme()

    def initialize_session_state(self):
        """Initialize session state for editing tasks.

        Precondition:
            - streamlit is downloaded and imported. 
           
        Postcondition:
            - editing_task and current_page are properly initialized in st.session_state.
            - editing_task is intilized to None.
            - current_page is intilized to 1.
        """
        if 'editing_task' not in st.session_state:
            st.session_state.editing_task = None
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 1

    def display_title(self):
        """Display the title of the application."""
        st.markdown("<h1 class='app-title'>Task Manager</h1>", unsafe_allow_html=True)

    def add_new_task(self):
        """Create a form for adding a new task.

        Precondition:
            - streamlit is downloaded and imported. 
            - Title and description cannot be blank or emptty.
        
        Postcondition:
            - New task is appended to the task list.

        Exceptions:
            - None

        Known issues:
            - "INFO: 127.0.0.1:35790 - "POST /tasks HTTP/1.1" 422 Unprocessable Entity" can show up and prevent task to be added   
        """
        st.markdown("## ✏️ Add New Task")
        title = st.text_input("Title", placeholder="Enter task title")
        tag = st.selectbox("Tag", ["Exam", "Assignment", "Labwork", "Project", "Other"])
        description = st.text_area("Description", placeholder="Enter task description")
        priority = st.radio("Priority", ["High", "Medium", "Low"], horizontal=True)

        if st.button("Add Task"):
            if title and description:
                priority_value = {"High": 1, "Medium": 2, "Low": 3}[priority]
                new_task = {
                    "title": title,
                    "description": description,
                    "priority": priority_value,
                    "tag": tag
                }
                self.task_manager.save_task(new_task)
                self.task_manager.load_tasks()  # Refresh task list
            else:
                st.warning("Title and description are required.")


    def view_tasks(self):
        """Display the list of tasks.

        Precondition:
            -  streamlit is downloaded and imported.
        
        Postcondition:
            - The tasks are displayed in a table format.
            - If no tasks exist, a message is displayed as "No tasks to display."

        Returns:
            - None
        """
        tasks = self.task_manager.tasks
        if not tasks:
            st.info("No tasks to display.")
            return

        # Pagination logic
        total_tasks = len(tasks)
        tasks_per_page = 10
        current_page = st.session_state.current_page
        start_idx = (current_page - 1) * tasks_per_page
        current_tasks = tasks[start_idx:start_idx + tasks_per_page]

        # Table headers0
        cols = st.columns([2, 1, 3, 1.5, 0.85, 1])
        for col, header in zip(cols, ["Title", "Tag", "Description", "Priority", "Edit", "Delete"]):
            with col:
                st.write(f"**{header}**")

        for i, task in enumerate(current_tasks, start=start_idx):
            self.display_task(task)

        if total_tasks > tasks_per_page:
            self.display_pagination_controls(total_tasks, current_page)


    def display_task(self, task):
        """Display an individual task in the table."""
        cols = st.columns([2, 1, 3, 1.5, 0.85, 1])
        with cols[0]:
            st.write(task['title'])
        with cols[1]:
            st.write(task.get('tag', 'Other'))  # Use default value for tag
        with cols[2]:
            st.write(task['description'])
        with cols[3]:
            priority_text = {1: "High", 2: "Medium", 3: "Low"}[task.get('priority', 2)]
            st.markdown(f"<div class='priority-{priority_text.lower()}'>{priority_text}</div>", unsafe_allow_html=True)
        with cols[4]:
            same_line_columns= st.columns([1, 3.5, 1])
            with same_line_columns[0]:
                if st.button("✏️", key=f"edit_{task['title']}"):
                    st.session_state.editing_task = task
            with same_line_columns[2]:
                if st.button("🗑️", key=f"delete_{task['id']}"):
                    self.task_manager.delete_task(task['id'])
                    self.task_manager.load_tasks()  # Refresh task list
        

    def edit_task(self):
        """Create a form for editing an existing task.
        
        Precondition:
        - streamlit is downloaded and imported. 
            
        Postcondition:
            - The tasks added is successfully edited and updated to the task list. 
        
        Exceptions:
            - If there's an error fetching tasks, raise RequestException with the error message.
        
        Known issues:
            - "INFO: 127.0.0.1:46460 - "PUT /tasks/111 HTTP/1.1" 500 Internal Server Error" shows up and prevent task to be updated
        """
        task = st.session_state.editing_task
        if task:
            st.markdown("## ✏️ Edit Task")
            title = st.text_input("Edit Title", value=task['title'])
            tag = st.selectbox("Edit Tag", ["Exam", "Assignment", "Labwork", "Project", "Other"], index=0)
            description = st.text_area("Edit Description", value=task['description'])
            priority_value = task.get('priority', 2)
            priority = st.radio("Edit Priority", ["High", "Medium", "Low"], index={1: 0, 2: 1, 3: 2}[priority_value])

            if st.button("Update Task"):
                updated_task = {
                    "title": title,
                    "description": description,
                    "priority": {"High": 1, "Medium": 2, "Low": 3}[priority],
                    "tag": tag
                }
                self.task_manager.update_task(task['id'], updated_task)
                st.session_state.editing_task = None
                self.task_manager.load_tasks()  # Refresh task list
                st.success("Task updated successfully!")


    def display_pagination_controls(self, total_tasks, current_page):
        """Display pagination controls for navigating through tasks."""
        cols = st.columns([1, 3, 1])
        with cols[0]:
            if st.button("Previous", disabled=current_page <= 1):
                st.session_state.current_page -= 1
                st.experimental_rerun()  # Refresh the app
        with cols[1]:
            st.write(
                f"Showing {((current_page - 1) * 10) + 1}-{min(current_page * 10, total_tasks)} of {total_tasks} tasks")
        with cols[2]:
            if st.button("Next", disabled=(current_page >= (total_tasks + 9) // 10)):
                st.session_state.current_page += 1
                st.experimental_rerun()  # Refresh the app

    def display_footer(self):
        """Display the footer of the application."""
        st.markdown("<div class='footer'>Task Manager © 2025</div>", unsafe_allow_html=True)

    def run(self):
        """Run the UI for the Task Manager."""
        self.display_title()
        if st.session_state.editing_task:
            self.edit_task()
        else:
            self.add_new_task()
        st.markdown("## 📋 Tasks")
        self.view_tasks()
        self.display_footer()


# Main function to run the Streamlit app
def main():
    """Main entry point for the Streamlit application."""
    task_manager = TaskManager()  # Initialize TaskManager communicating with FastAPI
    task_ui = TaskUI(task_manager)  # Initialize TaskUI
    task_ui.run()  # Run the UI


if __name__ == "__main__":
    main()

