import streamlit as st

def show_signup_page():
    st.title("Signup")
    
    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if new_username in st.session_state["users"]:
            st.error("Username already exists. Please choose a different one.")
        elif new_password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        elif new_username and new_password:
            st.session_state["users"][new_username] = new_password
            st.success("Signup successful! You can now log in.")
            st.session_state["page"] = "Login"
            st.rerun()
        else:
            st.error("All fields are required.")
