# ai_tutor_project/auth_component.py
import streamlit as st
from auth_manager import AuthManager

def auth_ui():
    st.sidebar.title("Secure Access")
    if st.sidebar.button("Login"):
        email = st.sidebar.text_input("Email")
        password = st.sidebar.text_input("Password", type="password")
        if AuthManager.login(email, password):
            st.session_state["user"] = email
            st.success(f"Logged in as {email}")
        else:
            st.error("Invalid credentials")
