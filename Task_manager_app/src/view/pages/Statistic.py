import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
from Styler import Styler

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

from controller.tasks import task_manager, TaskManager
from view.utils.auth import AuthGuard

# st.set_page_config(layout="centered")


def refresh_data(task_manager: TaskManager) -> pd.DataFrame:
    task_manager.load_tasks()
    tasks = task_manager.to_dict()
    df = pd.DataFrame.from_dict(tasks["tasks"])
    return df


@AuthGuard.require_login
def main():
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True

    if st.button("Switch Theme"):
        st.session_state.dark_mode = not st.session_state.dark_mode

    Styler.apply_custom_theme(st.session_state.dark_mode)

    st.markdown("<h1 class='about' style='text-align: center; color: #FF69B4;'>Task Progress Bar</h1>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("Pie chart showing the statistics of tasks with priority levels.")

    class DataProcessing:
        def __init__(self, data_frame: pd.DataFrame) -> None:
            self.data_frame = data_frame

        def priority_count(self) -> int:
            if self.data_frame is None or self.data_frame.empty:
                return None
            return self.data_frame["priority"].value_counts()  # counting each priority level

        def pie_chart(self):
            priority_count = self.priority_count()
            if priority_count is None:
                st.markdown(
                    "<p style='background-color: #BDB76B; color: red; padding: 5px 15px; text-align: center;'>No Data To Display</p>",
                    unsafe_allow_html=True,
                )
                st.set_option("deprecation.showPyplotGlobalUse", False)
                return None

            index_to_name = {1: "High Priority", 2: "Medium Priority", 3: "Low Priority"}
            labels = [index_to_name.get(index, str(index)) for index in priority_count.index]
            myexplode = [0.025] * len(priority_count)  # make the slices detached with a gap between them
            sizes = priority_count.values  # determine number of slices
            fig1, ax1 = plt.subplots()
            ax1.pie(
                sizes, labels=labels, autopct="%1.0f%%", colors=["red", "orange", "yellow"], explode=myexplode, startangle=30
            )
            plt.axis("equal")  # ensure the pie is a perfect circle
            ax1.set_facecolor("black")  # Set the background color to black
            return fig1

    if st.button("Refresh Data"):
        df = refresh_data(task_manager)
        data_processor = DataProcessing(df)
        fig1 = data_processor.pie_chart()
        if fig1:
            st.pyplot(fig1)
        st.rerun()

    df = refresh_data(task_manager)

    if df is not None:
        st.write(df.head())

    data_processor = DataProcessing(df)
    fig1 = data_processor.pie_chart()
    if fig1:
        st.pyplot(fig1)


main()
