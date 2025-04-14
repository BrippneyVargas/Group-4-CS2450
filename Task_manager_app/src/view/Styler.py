from configparser import ConfigParser
import streamlit as st
import os

class Styler:
    """Apply custom CSS styles for the application."""
    config_object = ConfigParser()

    @staticmethod
    def refresh():
        config_path = os.path.join(os.path.dirname(__file__), "..", "config.ini")
        Styler.config_object.read(config_path)


    @staticmethod
    def apply_custom_theme(dark_mode: bool): #Change the two modes to a composition.
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
        Styler.refresh()
        priority_info = Styler.config_object["PRIORITY"]
        theme_info = None
        if dark_mode: 
            theme_info = Styler.config_object["DARKMODE"]
            darkmode_css = f"""
            <style>
            body, .stApp {{ overflow: hidden !important; max-height: 100vh; }}
            .stApp {{ background-color: {theme_info["dark_background_color"]}; max-width: 100vw !important; margin: 0; padding: 0; }}
            ::-webkit-scrollbar {{ display: none; }}
            .priority-high {{ background-color: {priority_info["high"]}; color: white; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-medium {{ background-color: {priority_info["medium"]} !important; color: white !important; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-low {{ background-color: {priority_info["low"]}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 20px 0; color: {theme_info["primary_light"]}; font-size: 0.9em; background-color: {theme_info["dark_background_color"]}; }}
            .app-title {{ color: {theme_info["primary_light"]}; text-align: center; font-size: 3.5em; margin-bottom: 20px; font-weight: bold; }}
            </style>
            """
            st.markdown(darkmode_css, unsafe_allow_html=True)


        else: 
            theme_info = Styler.config_object["LIGHTMODE"]
            lightmode_css = f"""
            <style>
            .stRadio label[for="High"] {{ color: black !important; }}
            body, .stApp {{ overflow: hidden !important; max-height: 100vh; }}
            .stApp {{ background-color: {theme_info['light_background_color']} !important; max-width: 100%; max-height: 100%; margin: 0 auto; padding: 0 20px; color: {theme_info["text_color"]}; }}
            ::-webkit-scrollbar {{ display: none; }}
            div.stTextInput label {{ background-color: {theme_info['light_background_color']}; color: {theme_info['text_color']}; }}
            div.stTextInput input {{background-color: white; color: black}}
            div.stSelectbox label {{ background-color: {theme_info['light_background_color']}; color: {theme_info['text_color']}; }}
            div[data-baseweb="select"] > div {{background-color: white; color: black}}
            #root > div:nth-child(n) > div > div > div > div > div > div > ul li[aria-selected="true"] {{background-color: #FF99FF; color: black !important;}}
            #root > div:nth-child(2) > div > div > div > div > div > div > ul {{background-color: white;}}
            #root > div:nth-child(2) > div > div > div > div > div > div > ul div {{color: black;}}
            #root > div:nth-child(2) > div > div > div > div > div > div > ul li:hover {{background-color: #FFCCFF;}}
            div[data-baseweb="select"] svg[data-baseweb="icon"] {{fill: #FF99FF;}}
            div.stTextArea label {{ background-color: {theme_info['light_background_color']}; color: {theme_info['text_color']}; }}
            div.stTextArea textarea {{background-color: white; color: black}}
            div.stRadio > label {{ background-color: {theme_info['light_background_color']}; color: {theme_info['text_color']}; }}     
            .priority-high {{ background-color: {priority_info['high']}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-medium {{ background-color: {priority_info['medium']}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .priority-low {{ background-color: {priority_info['low']}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .stButton > button {{ background-color: {theme_info['button_color']}; color: black; padding: 5px 10px; border-radius: 5px; text-align: center; }}
            .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 20px 0; color: {theme_info['primary_light']}; font-size: 0.9em; background-color: {theme_info['light_background_color']}; }}
            .app-title {{ color: {theme_info['primary_light']}; text-align: center; font-size: 3.5em; margin-bottom: 20px; font-weight: bold; }}
            </style>
            """
            st.markdown(lightmode_css, unsafe_allow_html=True)
