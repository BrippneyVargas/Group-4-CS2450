import streamlit as st
import json
from model.task import Task
from model.task_manager import TaskManager


class TaskColor:
    """
    A utility class that defines a consistent color palette for the Task Manager application.

    This class encapsulates a set of carefully chosen colors to create a cohesive and
    visually appealing design across the application. The colors are selected to provide
    clear visual hierarchy, improve readability, and create an aesthetically pleasing
    user interface.
    """
    BACKGROUND_DARK = '#121212'
    PRIMARY_LIGHT = '#7BDFF2'  # Light blue
    SECONDARY_PINK = '#B54F5F'  # Muted pink
    TERTIARY_BLUE = '#4B5FBF'  # Deep blue
    ACCENT_LAVENDER = '#9381FF'  # Lavender
    HIGH_PRIORITY = '#FF4136'  # Bright Red
    MEDIUM_PRIORITY = '#FF851B'  # Orange
    LOW_PRIORITY = '#FFDC00'  # Yellow


class TaskStyler:
    """
    Manages application styling and custom CSS.

    Provides methods to apply a custom theme to the Streamlit application,
    controlling the overall look and feel, including background colors,
    scrollbar behavior, and priority-based color styling.
    """

    @staticmethod
    def apply_custom_theme():
        """
        Apply custom CSS for theme.

        Sets up a consistent visual style across the application,
        including scrollbar handling, color schemes, and priority-based styling.
        """
        custom_css = f"""
        <style>
        body, .stApp {{
            overflow: hidden !important;
            max-height: 100vh;
        }}

        .stApp {{
            background-color: {TaskColor.BACKGROUND_DARK};
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            overflow-y: auto !important;
        }}

        ::-webkit-scrollbar {{
            display: none;
        }}

        .stApp {{
            -ms-overflow-style: none;
            scrollbar-width: none;
        }}

        .priority-high {{
            background-color: {TaskColor.HIGH_PRIORITY};
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            text-align: center;
        }}

        .priority-medium {{
            background-color: {TaskColor.MEDIUM_PRIORITY};
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            text-align: center;
        }}

        .priority-low {{
            background-color: {TaskColor.LOW_PRIORITY};
            color: black;
            padding: 5px 10px;
            border-radius: 5px;
            text-align: center;
        }}
         .footer {{
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 20px 0;
            color: {TaskColor.PRIMARY_LIGHT};
            font-size: 0.9em;
            background-color: {TaskColor.BACKGROUND_DARK};
            z-index: 1000;
        }}

        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)


class TaskManagerApp:
    """
    The main application class for the Task Manager Streamlit interface.

    Handles the entire task management application, including initialization,
    UI rendering, task manipulation, and persistence. Provides methods for
    adding, viewing, saving, and loading tasks with a user-friendly interface.
    """

    def __init__(self):
        """
        Initialize the Streamlit Task Manager application.

        Configures page settings, initializes task manager, and applies custom styling.
        Sets up the basic structure and appearance of the application.
        """
        st.set_page_config(
            page_title="Task Manager",
            page_icon="📋",
            layout="wide",
            initial_sidebar_state="collapsed",
            menu_items=None
        )

        # Initialize task manager
        self._initialize_task_manager()

        # Apply custom styling
        TaskStyler.apply_custom_theme()

    def _initialize_task_manager(self):
        """
        Safely initialize task manager in session state.

        Ensures that the task manager is properly set up in the Streamlit
        session state, creating it if it doesn't exist and ensuring
        the tasks list is initialized.
        """
        if 'task_manager' not in st.session_state:
            st.session_state.task_manager = TaskManager()

        # Ensure tasks are of correct type
        if not hasattr(st.session_state.task_manager, 'tasks'):
            st.session_state.task_manager.tasks = []

    def display_footer(self):
        """
        Display application footer.

        Renders a centered footer with copyright information.
        """
        st.markdown("""
          <div class="footer">
              Task Manager © 2025   
          </div>
          """, unsafe_allow_html=True)

    def add_new_task(self, mgr: TaskManager):
        """
        Render the task add/edit form.

        Provides a user interface for creating new tasks or editing existing ones.
        Handles form input, validation, and task creation/update logic.

        Args:
            mgr (TaskManager): The task manager instance to add or update tasks.
        """
        st.markdown("<div class='task-container'>", unsafe_allow_html=True)

        # Check if editing an existing task
        editing_task = st.session_state.get('editing_task')

        # Form title and initial values
        st.markdown("## 📝 Edit Task" if editing_task else "## 📝 Add New Task")

        # Safely get values, defaulting to empty string or default values
        title = st.text_input("Title",
                              value=getattr(editing_task, 'title', '') if editing_task else '',
                              placeholder="Enter task title")

        tag_options = ["Exam", "Assignment", "Labwork", "Project", "Other"]

        # Safely get tag, defaulting to first option if not found
        current_tag = getattr(editing_task, 'tag', 'Assignment') if editing_task else 'Assignment'
        tag_index = tag_options.index(current_tag) if current_tag in tag_options else 0
        tag = st.selectbox("Tag", tag_options, index=tag_index)

        description = st.text_area("Description",
                                   value=getattr(editing_task, 'desc', '') if editing_task else '',
                                   placeholder="Enter task description")

        # Safely determine priority
        priority_options = ["High", "Medium", "Low"]
        if editing_task:
            priority_text = "High" if editing_task.priority == 1 else "Medium" if editing_task.priority == 2 else "Low"
        else:
            priority_text = "Medium"

        priority = st.radio("Priority", priority_options,
                            index=priority_options.index(priority_text),
                            horizontal=True)

        # Button actions
        col1, col2 = st.columns([1, 1])
        with col1:
            action_text = "Update Task" if editing_task else "Add Task"
            if st.button(action_text):
                if title:
                    # Convert priority to numeric value
                    priority_value = 1 if priority == "High" else 2 if priority == "Medium" else 3

                    # Create new task
                    new_task = Task(title=title, desc=description, priority=priority_value)
                    new_task.tag = tag  # Set the tag separately

                    if editing_task:
                        # Remove existing task and add updated task
                        mgr.tasks = [task for task in mgr.tasks if task.title != editing_task.title]

                    mgr.tasks.append(new_task)

                    # Clear editing state if present
                    if 'editing_task' in st.session_state:
                        del st.session_state.editing_task

                    st.rerun()
                else:
                    st.warning("Title is required.")

        with col2:
            if editing_task and st.button("Cancel"):
                del st.session_state.editing_task
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    def view_tasks(self, mgr: TaskManager):
        """
        Render the task list with pagination.

        Displays tasks in a tabular format with options to edit or delete.
        Implements basic pagination to handle large numbers of tasks.

        Args:
            mgr (TaskManager): The task manager instance containing tasks to display.
        """
        tasks = mgr.tasks if hasattr(mgr, 'tasks') else []

        if not tasks:
            st.info("No tasks to display.")
            return

        # Table headers
        col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 3, 1, 0.5, 0.5])
        headers = ["Title", "Tag", "Description", "Priority", "Edit", "Delete"]
        for col, header in zip([col1, col2, col3, col4, col5, col6], headers):
            with col:
                st.write(f"**{header}**")

        # Pagination setup ---> deep implementation in the future
        tasks_per_page = 10
        total_tasks = len(tasks)
        current_page = st.session_state.get('current_page', 1)
        start_idx = (current_page - 1) * tasks_per_page
        end_idx = min(start_idx + tasks_per_page, total_tasks)
        current_tasks = tasks[start_idx:end_idx]

        # Render tasks
        for i, task in enumerate(current_tasks, start=start_idx):
            col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 3, 1, 0.5, 0.5])

            with col1:
                st.write(task.title if hasattr(task, 'title') else 'N/A')
            with col2:
                st.write(task.tag if hasattr(task, 'tag') else 'N/A')
            with col3:
                st.write(task.desc if hasattr(task, 'desc') else 'N/A')
            with col4:
                priority_text = "High" if task.priority == 1 else "Medium" if task.priority == 2 else "Low"
                st.markdown(f"<div class='priority-{priority_text.lower()}'>{priority_text}</div>",
                            unsafe_allow_html=True)
            with col5:
                if st.button("✏️", key=f"edit_{i}"):
                    st.session_state.editing_task = task
            with col6:
                if st.button("🗑️", key=f"delete_{i}"):
                    if hasattr(task, 'title'):
                        mgr.tasks = [t for t in mgr.tasks if t.title != task.title]
                    st.rerun()

        # Pagination controls --> future implementation
        if total_tasks > tasks_per_page:
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                if st.button("Previous", disabled=current_page <= 1):
                    st.session_state.current_page = current_page - 1
                    st.rerun()
            with col2:
                st.write(f"Showing {start_idx + 1}-{end_idx} of {total_tasks} tasks")
            with col3:
                total_pages = (total_tasks + tasks_per_page - 1) // tasks_per_page
                if st.button("Next", disabled=current_page >= total_pages):
                    st.session_state.current_page = current_page + 1
                    st.rerun()

    def save_tasks(self, mgr: TaskManager):
        """
        Save tasks to a file.

        Serializes tasks to a JSON file for persistent storage.
        Handles potential file writing errors.

        Args:
            mgr (TaskManager): The task manager instance to save tasks from.
        """
        try:
            with open("src/cli/tasks.json", 'w') as f:
                json.dump([task.to_dict() for task in mgr.tasks], f, indent=4)
            st.success("Tasks saved successfully!")
        except Exception as e:
            st.error(f"Error saving tasks: {e}")

    def load_tasks(self, mgr: TaskManager):
        """
        Load tasks from a file.

        Reads tasks from a JSON file and reconstructs Task objects.
        Handles potential file reading and parsing errors.

        Args:
            mgr (TaskManager): The task manager instance to load tasks into.
        """
        try:
            with open("src/cli/tasks.json", 'r') as f:
                task_data = json.load(f)
                # Convert loaded data to Task objects
                mgr.tasks = [
                    Task(
                        title=task['Title'],
                        desc=task['Description'],
                        priority=task['Priority']
                    ) for task in task_data
                ]
            st.success("Tasks loaded successfully!")
            st.rerun()
        except FileNotFoundError:
            st.warning("No saved tasks found.")
        except json.JSONDecodeError:
            st.error("Error decoding tasks file. File might be corrupted.")
        except Exception as e:
            st.error(f"Error loading tasks: {e}")

    def display_header(self):
        """
        Display application header.

        Renders a styled header for the Task Manager application,
        providing a visually appealing title.
        """
        st.markdown("""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="color: #7BDFF2; font-size: 2.5em;">📋 Task Manager</h1>
        </div>
        """, unsafe_allow_html=True)

    def display_save_load_buttons(self, mgr: TaskManager):
        """
        Display save and load task buttons.

        Creates buttons for saving and loading tasks, providing
        user interface for task persistence.

        Args:
            mgr (TaskManager): The task manager instance for save/load operations.
        """
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            pass  # Placeholder to maintain layout
        with col2:
            if st.button("💾 Save Tasks"):
                self.save_tasks(mgr)
        with col3:
            if st.button("📂 Load Tasks"):
                self.load_tasks(mgr)

    def handle_choice(self, mgr: TaskManager):
        """
        Render the entire application interface.

        Orchestrates the entire application UI by calling methods
        to display header, save/load buttons, task form, and task list.

        Args:
            mgr (TaskManager): The task manager instance to pass to UI components.
        """
        # Add horizontal header
        self.display_header()

        # Header with Save and Load Tasks buttons
        self.display_save_load_buttons(mgr)

        # Render task form and task list
        self.add_new_task(mgr)

        # Add Tasks section title
        st.markdown("## 📋 Tasks")

        # Render task list
        self.view_tasks(mgr)

        # Add footer
        self.display_footer()

    def run(self):
        """
        Main application entry point.

        Triggers the task management interface by calling handle_choice
        with the current task manager from session state.
        """
        self.handle_choice(st.session_state.task_manager)


def main():
    """
    Entry point for the Streamlit application.

    Creates an instance of TaskManagerApp and runs the application.
    """
    app = TaskManagerApp()
    app.run()


if __name__ == "__main__":
    main()