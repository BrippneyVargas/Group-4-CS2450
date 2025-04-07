import streamlit as st
from Task_manager_app.src.view.Styler import Styler

st.set_page_config(layout="centered")

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

if st.button("Switch Theme"):
    st.session_state.dark_mode = not st.session_state.dark_mode

Styler.apply_custom_theme(st.session_state.dark_mode)

st.markdown("<h1 class='about' style='text-align: center; color: #FF69B4;'>Log In</h1>", unsafe_allow_html=True)
st.markdown("\n")
st.text_input("Username", placeholder="Enter your username")
st.text_input("Password", placeholder="Enter your password", type="password")

st.col1, st.col2 = st.columns(2)
with st.col1:
    st.button("Log In")
with st.col2:
    st.markdown("Don't have an account? [Sign Up](/signup)")