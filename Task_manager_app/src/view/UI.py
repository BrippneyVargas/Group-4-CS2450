import streamlit as st
import time

# st.set_page_config(layout="centered")


class UI:
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
        if "tasks" not in st.session_state:
            self.task_manager.load_tasks()
        if "editing_task" not in st.session_state:
            st.session_state.editing_task = None
        if "current_page" not in st.session_state:
            st.session_state.current_page = 1

    def display_title(self):
        """Display the title of the application."""
        st.markdown("<h1 class='app-title'>TaskZen</h1>", unsafe_allow_html=True)
        st.markdown(
            "<h5 class='app-slogan' style='text-align: center; color: orange;'>A Task Manager that keeps you on track and organized.</h5>",
            unsafe_allow_html=True,
        )
        st.markdown("\n")

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
                priority_value = {":red[High]": 1, ":orange[Medium]": 2, ":green[Low]": 3}[priority]
                new_task = {
                    "id": len(self.task_manager.tasks) + 1,
                    "title": title,
                    "description": description,
                    "priority": priority_value,
                    "tag": tag,
                }

                self.task_manager.save_task(new_task)
                self.task_manager.load_tasks()
            else:
                st.markdown(
                    "<p style='background-color: #BDB76B; color: red;'>&nbsp;&nbsp;Title and description are required.</p>",
                    unsafe_allow_html=True,
                )

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
            st.markdown(
                "<p style= 'background-color: rgba(60, 179, 113, 0.5); padding: 10px;''>&nbsp;&nbsp;No tasks to display.</p>",
                unsafe_allow_html=True,
            )
            return

        # Pagination logic
        total_tasks = len(tasks)
        tasks_per_page = 10
        current_page = st.session_state.current_page
        start_idx = (current_page - 1) * tasks_per_page
        current_tasks = tasks[start_idx : start_idx + tasks_per_page]

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
            st.write(task.title)
        with cols[1]:
            st.write(task.tag if task.tag else "Other")
        with cols[2]:
            st.write(task.description)
        with cols[3]:
            priority_value = task.priority if task.priority is not None else 2
            priority_text = {1: "High", 2: "Medium", 3: "Low"}[priority_value]
            st.markdown(f"<div class='priority-{priority_text.lower()}'>{priority_text}</div>", unsafe_allow_html=True)
        with cols[4]:
            same_line_columns = st.columns([1, 3.5, 1])
            with same_line_columns[0]:
                if st.button("✏️", key=f"edit_{task.id}"):
                    st.session_state.editing_task = task
                    time.sleep(0.05)
                    st.rerun()
            with same_line_columns[2]:
                if st.button("🗑️", key=f"delete_{task.id}"):
                    self.task_manager.delete_task(task.id)
                    time.sleep(0.05)
                    self.task_manager.load_tasks()  # Refresh task list
                    st.rerun()  # Trigger a rerun to update the UI

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
            st.markdown("## ✏️ :green[Edit] :violet[Task]")
            title = st.text_input("Edit Title", value=task.title)
            tag = st.selectbox("Edit Tag", ["Exam", "Assignment", "Labwork", "Project", "Other"], index=0)
            description = st.text_area("Edit Description", value=task.description)
            priority_value = task.priority if task.priority is not None else 2
            priority = st.radio(
                "Edit Priority", [":red[High]", ":orange[Medium]", ":green[Low]"], index={1: 0, 2: 1, 3: 2}[priority_value]
            )

            if st.button("Update Task"):
                updated_task = {
                    "id": task.id,
                    "title": title,
                    "description": description,
                    "priority": {":red[High]": 1, ":orange[Medium]": 2, ":green[Low]": 3}[priority],
                    "tag": tag,
                }
                self.task_manager.update_task(task.id, updated_task)
                st.session_state.editing_task = None
                self.task_manager.load_tasks()  # Refresh task list
                st.markdown(
                    "<p style= 'background-color: rgba(60, 179, 113, 0.5); padding: 10px;'>Tasks updated sucessfully</p>",
                    unsafe_allow_html=True,
                )

    def display_pagination_controls(self, total_tasks, current_page):
        """Display pagination controls for navigating through tasks."""
        cols = st.columns([1, 3, 1])
        with cols[0]:
            if st.button("Previous", disabled=current_page <= 1):
                st.session_state.current_page -= 1
        with cols[1]:
            st.write(f"Showing {((current_page - 1) * 10) + 1}-{min(current_page * 10, total_tasks)} of {total_tasks} tasks")
        with cols[2]:
            if st.button("Next", disabled=(current_page >= (total_tasks + 9) // 10)):
                st.session_state.current_page += 1

    def display_footer(self):
        """Display the footer of the application."""
        st.markdown("<div class='footer'>TaskZen © 2025</div>", unsafe_allow_html=True)

    def display_save_load_buttons(self):
        """Display buttons for saving and loading tasks."""
        cols = st.columns([3, 1, 1])
        with cols[0]:
            # Just a placeholder for checking if API is available
            st.markdown(
                "<p style= 'background-color: rgba(60, 179, 113, 0.5); padding: 10px;'>✅ API Connected</p>",
                unsafe_allow_html=True,
            )
        with cols[1]:
            if st.button("💾 Save Tasks"):
                if self.task_manager.tasks:
                    st.markdown(
                        "<p style= 'background-color: rgba(60, 179, 113, 0.5); padding: 10px;'>Tasks saved sucessfully</p>",
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        "<p style='background-color: #BDB76B; color: red;'>&nbsp;&nbsp;No tasks to save</p>",
                        unsafe_allow_html=True,
                    )
        with cols[2]:
            if st.button("📂 Load Tasks"):
                self.task_manager.load_tasks()
                st.markdown(
                    "<p style='background-color: rgba(60, 179, 113, 0.5); padding: 10px;'>Tasks loaded successfully!</p>",
                    unsafe_allow_html=True,
                )

    def run(self):
        """Run the UI for the Task Manager."""
        self.display_title()
        st.sidebar
        self.display_save_load_buttons()
        if st.session_state.editing_task:
            self.edit_task()
        else:
            self.add_new_task()
        st.markdown("## 📋 :orange[T]:green[a]:red[s]:blue[k]:violet[s]")
        self.view_tasks()
        self.display_footer()
