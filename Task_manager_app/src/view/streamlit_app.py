#view/streamlit_app.py
import streamlit as st
import requests


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
    """Manage the tasks, including API interactions."""

    def __init__(self, api_url):
        self.api_url = api_url
        self.tasks = []

    def fetch_tasks(self):
        """Fetch tasks from the FastAPI backend."""
        try:
            response = requests.get(f"{self.api_url}/tasks")
            response.raise_for_status()
            self.tasks = response.json().get('tasks', [])
        except requests.RequestException as e:
            st.error(f"Error fetching tasks: {e}")

    def save_task(self, task):
        """Save a new task to the API."""
        with st.spinner("Saving task..."):
            try:
                response = requests.post(f"{self.api_url}/tasks", json=task)
                response.raise_for_status()
                task['id'] = response.json()['task']['id']  # Get task ID from response
                self.tasks.append(task)  # Add task to list
                st.success("Task added successfully!")
            except requests.RequestException as e:
                st.error(f"Error saving task: {e}")

    def load_tasks(self):
        """Load tasks from the FastAPI backend."""
        self.fetch_tasks()  # Re-fetch tasks
        st.success("Tasks loaded successfully!")

    def update_task(self, task_id, updated_task):
        """Update a task identified by task_id."""
        with st.spinner("Updating task..."):
            try:
                response = requests.put(f"{self.api_url}/tasks/{task_id}", json=updated_task)
                response.raise_for_status()
                st.success("Task updated successfully!")
                self.fetch_tasks()  # Refresh task list after update
            except requests.RequestException as e:
                st.error(f"Error updating task: {e}")

    def delete_task(self, task):
        """Delete a task."""
        with st.spinner("Deleting task..."):
            try:
                response = requests.delete(f"{self.api_url}/tasks/{task['id']}")
                if response.status_code == 200:
                    st.success("Task deleted successfully!")
                    self.tasks.remove(task)  # Remove from list
                else:
                    st.error("Error deleting task.")
            except requests.RequestException as e:
                st.error(f"Error when attempting to delete task: {e}")


class TaskUI:
    """Manage the user interface for the Task Manager."""

    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.initialize_session_state()
        TaskStyler.apply_custom_theme()

    def initialize_session_state(self):
        """Initialize session state for the application."""
        if 'editing_task' not in st.session_state:
            st.session_state.editing_task = None
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 1

    def display_title(self):
        """Display the title of the application."""
        st.markdown("<h1 class='app-title'>Task Manager</h1>", unsafe_allow_html=True)

    def add_new_task(self):
        """Create a form for adding a new task."""
        st.markdown("## ✏️ Add New Task")
        title = st.text_input("Title", placeholder="Enter task title")
        tag = st.selectbox("Tag", ["Exam", "Assignment", "Labwork", "Project", "Other"])
        description = st.text_area("Description", placeholder="Enter task description")
        priority = st.radio("Priority", ["High", "Medium", "Low"], horizontal=True)

        if st.button("Add Task"):
            if title:
                priority_value = {"High": 1, "Medium": 2, "Low": 3}[priority]
                new_task = {
                    "title": title,
                    "description": description,
                    "priority": priority_value,
                    "tag": tag
                }
                self.task_manager.save_task(new_task)  # Save the task
            else:
                st.warning("Title is required.")

    def view_tasks(self):
        """Display the list of tasks."""
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

        # Table headers
        cols = st.columns([2, 1, 3, 1, 0.5])
        for col, header in zip(cols, ["Title", "Tag", "Description", "Priority", "Actions"]):
            with col:
                st.write(f"**{header}**")

        for i, task in enumerate(current_tasks, start=start_idx):
            self.display_task(task, i)

        if total_tasks > tasks_per_page:
            self.display_pagination_controls(total_tasks, current_page)

    def display_task(self, task, index):
        """Display an individual task in the table."""
        cols = st.columns([2, 1, 3, 1, 0.5])
        with cols[0]:
            st.write(task['title'])
        with cols[1]:
            st.write(task['tag'])
        with cols[2]:
            st.write(task['description'])
        with cols[3]:
            priority_text = {1: "High", 2: "Medium", 3: "Low"}[task['priority']]
            st.markdown(f"<div class='priority-{priority_text.lower()}'>{priority_text}</div>", unsafe_allow_html=True)
        with cols[4]:
            if st.button("✏️ Edit", key=f"edit_{index}"):
                st.session_state.editing_task = task
                self.edit_task(task)
            if st.button("🗑️ Delete", key=f"delete_{index}"):
                self.task_manager.delete_task(task)

    def edit_task(self, task):
        """Create a form for editing an existing task."""
        if task:
            title = st.text_input("Edit Title", value=task['title'])
            tag = st.selectbox("Edit Tag", ["Exam", "Assignment", "Labwork", "Project", "Other"],
                               index=["Exam", "Assignment", "Labwork", "Project", "Other"].index(task['tag']))
            description = st.text_area("Edit Description", value=task['description'])
            priority = st.radio("Edit Priority", ["High", "Medium", "Low"],
                                index={"High": 1, "Medium": 2, "Low": 3}[task['priority']])

            if st.button("Update Task"):
                updated_task = {
                    "title": title,
                    "description": description,
                    "priority": {"High": 1, "Medium": 2, "Low": 3}[priority],
                    "tag": tag
                }
                self.task_manager.update_task(task['id'], updated_task)  # Pass task ID
                st.session_state.editing_task = None
                self.task_manager.fetch_tasks()  # Refresh task list

    def display_pagination_controls(self, total_tasks, current_page):
        """Display pagination controls for navigating through tasks."""
        cols = st.columns([1, 3, 1])
        with cols[0]:
            if st.button("Previous", disabled=current_page <= 1):
                st.session_state.current_page -= 1
                st.experimental_rerun()
        with cols[1]:
            st.write(
                f"Showing {((current_page - 1) * 10) + 1}-{min(current_page * 10, total_tasks)} of {total_tasks} tasks")
        with cols[2]:
            if st.button("Next", disabled=(current_page >= (total_tasks + 9) // 10)):  # Ceiling division
                st.session_state.current_page += 1
                st.experimental_rerun()

    def display_footer(self):
        """Display the footer of the application."""
        st.markdown("<div class='footer'>Task Manager © 2025</div>", unsafe_allow_html=True)

    def run(self):
        """Run the UI for the Task Manager."""
        self.display_title()

        # Create a row of buttons side by side for saving and loading tasks
        cols = st.columns(2)
        with cols[0]:
            if st.button("Save Tasks"):
                self.task_manager.load_tasks()  # Load tasks to refresh the list

        with cols[1]:
            if st.button("Load Tasks"):
                self.task_manager.load_tasks()

        self.add_new_task()
        st.markdown("## 📋 Tasks")
        self.view_tasks()
        self.display_footer()


# Main function to run the Streamlit app
def main():
    """Main entry point for the Streamlit application."""
    task_manager = TaskManager(api_url="http://127.0.0.1:8000")  # Initialize TaskManager
    task_ui = TaskUI(task_manager)  # Initialize TaskUI
    task_ui.run()  # Run the UI


if __name__ == "__main__":

    main()