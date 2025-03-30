import streamlit as st

st.set_page_config(layout="centered")

st.title("Log In Page")
st.markdown("\n")
st.text_input("Username", placeholder="Enter your username")
st.text_input("Password", placeholder="Enter your password", type="password")

st.col1, st.col2 = st.columns(2)
with st.col1:
    st.button("Log In")
with st.col2:
    st.markdown("Don't have an account? [Sign Up](/signup)")