import streamlit as st
from Styler import Styler


class AuthGuard:
    @staticmethod
    def require_login(func):
        def wrapper(*args, **kwargs):
            st.set_page_config(layout="centered")

            # Handle dark mode theme globally
            if "dark_mode" not in st.session_state:
                st.session_state.dark_mode = True
            if st.button("Switch Theme"):
                st.session_state.dark_mode = not st.session_state.dark_mode
            Styler.apply_custom_theme(st.session_state.dark_mode)

            # Check login state
            if not st.session_state.get("logged_in", False):
                AuthGuard.show_login_form()
                return  # Prevent running the main app
            else:
                return func(*args, **kwargs)

        return wrapper

    @staticmethod
    def show_login_form():
        st.markdown("<h1 class='about' style='text-align: center; color: #FF69B4;'>Log In</h1>", unsafe_allow_html=True)
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", placeholder="Enter your password", type="password")
            submitted = st.form_submit_button("Log In")
            if submitted:
                # Replace this with real user auth if needed
                if username == "admin" and password == "password":
                    st.session_state.logged_in = True
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password.")
        st.markdown("Don't have an account? [Sign Up](/signup)")
