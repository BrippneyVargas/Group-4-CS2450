import streamlit as st
from Styler import Styler

st.set_page_config(layout="centered")

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

if st.button("Switch Theme"):
    st.session_state.dark_mode = not st.session_state.dark_mode

Styler.apply_custom_theme(st.session_state.dark_mode)


st.markdown("<h1 class='about' style='text-align: center; color: #FF69B4;'>About TaskZen</h1>", unsafe_allow_html=True)
st.markdown("")
st.markdown(
    """
    TaskZen is a simple yet powerful task manager designed to help you stay organized and on top of your responsibilities. Whether you're handling assignments, projects, exams, or personal tasks, TaskZen provides an easy-to-use interface to add, view, edit, and delete tasks. You can categorize your tasks with tags, set priorities, and track your progress all in one place. 

    Key Features:
    - **Add new tasks**: Create tasks with titles, descriptions, tags, and priorities.
    - **View and manage tasks**: See your tasks in a table with pagination for easy navigation.
    - **Edit tasks**: Update tasks with new information or modify existing details.
    - **Delete tasks**: Remove tasks when they’re completed or no longer needed.
    - **Save and load tasks**: Keep your tasks persistent with the option to save and load them.

    TaskZen helps you stay focused and productive, ensuring you never miss a deadline or forget a task again.

    <br>
    Built with ❤️ by Group 4 for CS 2450.
    """
     , unsafe_allow_html=True)



