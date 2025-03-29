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
    ## Dark Mode Color
    BACKGROUND_DARK = '#121212'
    PRIMARY_LIGHT = '#7BDFF2'
    HIGH_PRIORITY = '#FF4136'
    MEDIUM_PRIORITY = '#FF851B'
    LOW_PRIORITY = '#FFDC00'

    # #Light Mode Color
    BACKGROUND_LIGHT = '#FFFFFF'
    PRIMARY_LIGHT_LM = '#f20c59'
    TEXT_COLOR = 'blue'
    BUTTON_COLOR = '#FFCCFF'


class TaskStyler:
    """Apply custom CSS styles for the application."""

    @staticmethod
    def apply_custom_theme(dark_mode: bool):
        """
        Customize the Streamlit application with colors, theme and styles.

        Precondition:
                - streamlit is downloaded and imported.

        Postcondition:
            - The tasks are displayed in a table format.
            - If no tasks exist, a message is displayed as "No tasks to display."

        Known issues:
            - If streamlit package is not installed, there'll be an error: ModuleNotFoundError: No module named 'streamlit'

        """
        if dark_mode: 
            darkmode_css = f"""
            <style>
            body, .stApp {{ overflow: hidden !important; max-height: 100vh; }}
            .stApp {{ background-color: {TaskColor.BACKGROUND_DARK}; max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
            ::-webkit-scrollbar {{ display: none; }}
            .priority-high {{ background-color: {TaskColor.HIGH_PRIORITY}; color: white; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-medium {{ background-color: {TaskColor.MEDIUM_PRIORITY}; color: white; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-low {{ background-color: {TaskColor.LOW_PRIORITY}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 20px 0; color: {TaskColor.PRIMARY_LIGHT}; font-size: 0.9em; background-color: {TaskColor.BACKGROUND_DARK}; }}
            .app-title {{ color: {TaskColor.PRIMARY_LIGHT}; text-align: center; font-size: 3.5em; margin-bottom: 20px; font-weight: bold; }}
            </style>
            """
            st.markdown(darkmode_css, unsafe_allow_html=True)

        else: 
            lightmode_css = f"""
            <style>
            
            .stRadio label[for="High"] {{ color: black !important;}}
            body, .stApp {{ overflow: hidden !important; max-height: 100vh; }}
            .stApp {{ background-color: {TaskColor.BACKGROUND_LIGHT}; max-width: 100%; max-height: 100%; margin: 0 auto; padding: 0 20px; color: {TaskColor.TEXT_COLOR}; }}
            ::-webkit-scrollbar {{ display: none; }}
            div.stTextInput label {{ background-color: {TaskColor.BACKGROUND_LIGHT}; color: {TaskColor.TEXT_COLOR}; }}
            div.stTextInput input {{background-color: white; color: black}}
            div.stSelectbox label {{ background-color: {TaskColor.BACKGROUND_LIGHT}; color: {TaskColor.TEXT_COLOR}; }}
            div[data-baseweb="select"] > div {{background-color: white; color: black}}
            #root > div:nth-child(n) > div > div > div > div > div > div > ul li[aria-selected="true"] {{background-color: #FF99FF; color: black !important;}}
            #root > div:nth-child(2) > div > div > div > div > div > div > ul {{background-color: white;}}
            #root > div:nth-child(2) > div > div > div > div > div > div > ul div {{color: black;}}
            #root > div:nth-child(2) > div > div > div > div > div > div > ul li:hover {{background-color: #FFCCFF;}}
            div[data-baseweb="select"] svg[data-baseweb="icon"] {{fill: #FF99FF;}}
            div.stTextArea label {{ background-color: {TaskColor.BACKGROUND_LIGHT}; color: {TaskColor.TEXT_COLOR}; }}
            div.stTextArea textarea {{background-color: white; color: black}}
            div.stRadio > label {{ background-color: {TaskColor.BACKGROUND_LIGHT}; color: {TaskColor.TEXT_COLOR}; }}
            .priority-high {{ background-color: {TaskColor.HIGH_PRIORITY}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-medium {{ background-color: {TaskColor.MEDIUM_PRIORITY}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-low {{ background-color: {TaskColor.LOW_PRIORITY}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .stButton > button {{ background-color: {TaskColor.BUTTON_COLOR}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 20px 0; color: {TaskColor.PRIMARY_LIGHT_LM}; font-size: 0.9em; background-color: {TaskColor.BACKGROUND_LIGHT}; }}
            .app-title {{ color: {TaskColor.PRIMARY_LIGHT_LM}; text-align: center; font-size: 3.5em; margin-bottom: 20px; font-weight: bold; }}
            
            </style>
            """
            st.markdown(lightmode_css, unsafe_allow_html=True)


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
            if self.tasks:
                st.markdown("<p style='background-color: #3CB371'>Tasks loaded successfully!</p>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Unexpected error while loading tasks: {e}")


class TaskUI:
    """Manage the user interface for the Task Manager."""

    def __init__(self, task_manager):
        self.task_manager = task_manager

    def initialize_session_state(self):
        """Initialize session state for editing tasks.

        Precondition:
            - streamlit is downloaded and imported.

        Postcondition:
            - editing_task and current_page are properly initialized in st.session_state.
            - editing_task is initialized to None.
            - current_page is initialized to 1.
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
        st.markdown("## ✏️ :red[Add] :violet[New] :green[Task]")
        title = st.text_input("Title", placeholder="Enter task title")
        tag = st.selectbox("Tag", ["Exam", "Assignment", "Labwork", "Project", "Other"])
        description = st.text_area("Description", placeholder="Enter task description")
        priority = st.radio("Priority", [":red[High]", ":orange[Medium]", ":green[Low]"], horizontal=True)

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
                st.markdown("<p style='background-color: #BDB76B; color: red;'>&nbsp;&nbsp;Title and description are required.</p>", unsafe_allow_html=True)

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
            same_line_columns = st.columns([1, 3.5, 1])
            with same_line_columns[0]:
                if st.button("✏️", key=f"edit_{task['id']}"):
                    st.session_state.editing_task = task
            with same_line_columns[2]:
                if st.button("🗑️", key=f"delete_{task['id']}"):
                    self.task_manager.delete_task(task['id'])
                    self.task_manager.load_tasks()  # Refresh task list
                    if st.button("✅"):
                        st.write("")
    

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

    def display_save_load_buttons(self):
        """Display buttons for saving and loading tasks."""
        cols = st.columns([3, 1, 1])
        with cols[0]:
            # Just a placeholder for checking if API is available
            st.markdown("<p style='background-color: #3CB371'>✅ API Connected</p>", unsafe_allow_html=True)
        with cols[1]:
            if st.button("💾 Save Tasks"):
                if self.task_manager.tasks:
                    for task in self.task_manager.tasks:
                        self.task_manager.save_task(task)
                else:
                    st.markdown("<p style='background-color: #BDB76B; color: red;'>&nbsp;&nbsp;No tasks to save</p>", unsafe_allow_html=True)
        with cols[2]:
            if st.button("📂 Load Tasks"):
                self.task_manager.load_tasks()
                st.experimental_rerun()  # Refresh the app after loading

    def run(self):
        """Run the UI for the Task Manager."""
        self.display_title()
        self.display_save_load_buttons()
        if st.session_state.editing_task:
            self.edit_task()
        else:
            self.add_new_task()
        st.markdown("## 📋 :orange[T]:green[a]:red[s]:blue[k]:violet[s]")
        self.view_tasks()
        self.display_footer()


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



