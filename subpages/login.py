import streamlit as st

def show_login_page():
    st.title("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state["users"] and st.session_state["users"][username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["page"] = "Home"
            st.rerun()
        else:
            st.error("Invalid username or password")

    if st.button("Create New Account"):
        st.session_state["page"] = "Signup"
        st.rerun()
