import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import json
from Styler import Styler

st.set_page_config(layout="centered")

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

if st.button("Switch Theme"):
    st.session_state.dark_mode = not st.session_state.dark_mode

Styler.apply_custom_theme(st.session_state.dark_mode)

st.markdown("<h1 class='about' style='text-align: center; color: #FF69B4;'>Task Progress Bar</h1>", unsafe_allow_html=True)
st.markdown("")
st.markdown("Pie chart showing the statistics of tasks with priority levels.")

TASKS_FILE = "./Task_manager_app/src/model/tasks.json"


class DataFetching:
    def __init__(self, file_path: str) -> None:
        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            st.error(f"File not found: {file_path}")
            self.file_path = None
    
    def read_json_with_panda(self):
        try:
            with open(self.file_path, "r") as file: #handling nested dictionary in json
                data=json.load(file)
            if "tasks" in data:
                data_frame= pd.DataFrame(data["tasks"]) #extract tasks from json to panda dataframe
                return data_frame
        except ValueError as e:
            st.error(f"Error reading JSON file: {e}")
            return None


class DataProcessing:
    def __init__(self, data_frame: pd.DataFrame) -> None:
        self.data_frame = data_frame

    def priority_count(self):
        if self.data_frame is None or self.data_frame.empty:
            return None
        return self.data_frame["priority"].value_counts() #counting each priority levels

    def pie_chart(self):
        priority_count = self.priority_count()
        if priority_count is None:
            st.markdown("<p style='background-color: #BDB76B; color: red; padding: 5px 15px; text-align: center;'>No Data To Display</p>", unsafe_allow_html=True)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            return None

        index_to_name= {1: "High Priority", 2: "Medium Priority", 3: "Low Priority"}
        labels = [index_to_name[index] for index in priority_count.index]
        myexplode= [0.025] * len(priority_count) #make the slide detached or has a gap between each slide
        sizes = priority_count.values #determine number of slides
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.0f%%', colors=['red', 'orange', 'yellow'], explode=myexplode, startangle=30)
        plt.axis('equal')  #ensure the pie is a perfect circle 
        return fig1
    


data_fetcher = DataFetching(TASKS_FILE)
df = data_fetcher.read_json_with_panda()

if df is not None:
    st.write(df.head())  
 
data_processor = DataProcessing(df)
# st.write(data_processor.priority_count())
fig1 = data_processor.pie_chart()
st.pyplot(fig1)