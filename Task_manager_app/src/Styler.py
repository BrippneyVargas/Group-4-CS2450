import streamlit as st
from ThemeColor import *

class Styler:
    """Apply custom CSS styles for the application."""

    @staticmethod
    def apply_custom_theme(dark_mode: bool): #TODO Change the two modes to a composition.
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
            .stApp {{ background-color: {ThemeColor.BACKGROUND_DARK}; max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
            ::-webkit-scrollbar {{ display: none; }}
            .priority-high {{ background-color: {ThemeColor.HIGH_PRIORITY}; color: white; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-medium {{ background-color: {ThemeColor.MEDIUM_PRIORITY}; color: white; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-low {{ background-color: {ThemeColor.LOW_PRIORITY}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 20px 0; color: {ThemeColor.PRIMARY_LIGHT}; font-size: 0.9em; background-color: {ThemeColor.BACKGROUND_DARK}; }}
            .app-title {{ color: {ThemeColor.PRIMARY_LIGHT}; text-align: center; font-size: 3.5em; margin-bottom: 20px; font-weight: bold; }}
            </style>
            """
            st.markdown(darkmode_css, unsafe_allow_html=True)

        else: 
            lightmode_css = f"""
            <style>
            
            .stRadio label[for="High"] {{ color: black !important;}}
            body, .stApp {{ overflow: hidden !important; max-height: 100vh; }}
            .stApp {{ background-color: {ThemeColor.BACKGROUND_LIGHT}; max-width: 100%; max-height: 100%; margin: 0 auto; padding: 0 20px; color: {ThemeColor.TEXT_COLOR}; }}
            ::-webkit-scrollbar {{ display: none; }}
            div.stTextInput label {{ background-color: {ThemeColor.BACKGROUND_LIGHT}; color: {ThemeColor.TEXT_COLOR}; }}
            div.stTextInput input {{background-color: white; color: black}}
            div.stSelectbox label {{ background-color: {ThemeColor.BACKGROUND_LIGHT}; color: {ThemeColor.TEXT_COLOR}; }}
            div[data-baseweb="select"] > div {{background-color: white; color: black}}
            #root > div:nth-child(n) > div > div > div > div > div > div > ul li[aria-selected="true"] {{background-color: #FF99FF; color: black !important;}}
            #root > div:nth-child(2) > div > div > div > div > div > div > ul {{background-color: white;}}
            #root > div:nth-child(2) > div > div > div > div > div > div > ul div {{color: black;}}
            #root > div:nth-child(2) > div > div > div > div > div > div > ul li:hover {{background-color: #FFCCFF;}}
            div[data-baseweb="select"] svg[data-baseweb="icon"] {{fill: #FF99FF;}}
            div.stTextArea label {{ background-color: {ThemeColor.BACKGROUND_LIGHT}; color: {ThemeColor.TEXT_COLOR}; }}
            div.stTextArea textarea {{background-color: white; color: black}}
            div.stRadio > label {{ background-color: {ThemeColor.BACKGROUND_LIGHT}; color: {ThemeColor.TEXT_COLOR}; }}     
            .priority-high {{ background-color: {ThemeColor.HIGH_PRIORITY}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-medium {{ background-color: {ThemeColor.MEDIUM_PRIORITY}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-low {{ background-color: {ThemeColor.LOW_PRIORITY}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .stButton > button {{ background-color: {ThemeColor.BUTTON_COLOR}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 20px 0; color: {ThemeColor.PRIMARY_LIGHT_LM}; font-size: 0.9em; background-color: {ThemeColor.BACKGROUND_LIGHT}; }}
            .app-title {{ color: {ThemeColor.PRIMARY_LIGHT_LM}; text-align: center; font-size: 3.5em; margin-bottom: 20px; font-weight: bold; }}
            
            </style>
            """
            st.markdown(lightmode_css, unsafe_allow_html=True)
