import streamlit as st
from streamlit_option_menu import option_menu

# Importing subpages
from subpages import home, login, signup, check_health, parenting,consultation, resources, chatbot, contactus, settings

st.set_page_config(page_title="Maternal Health")

# ---- Initialize Session State ----
if "users" not in st.session_state:
    st.session_state["users"] = {"admin": "admin123"}
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "page" not in st.session_state:
    st.session_state["page"] = "Login"

# ---- Sidebar Navigation ----
if st.session_state["logged_in"]:
    with st.sidebar:
        selected_menu = option_menu(
            menu_title="NurtureNest ",
            options=["Home", "Check Health", "Doctor Consultation", "Resources","Parenting Classes", "Chatbot", "contactus", "Settings", "Logout"],
            icons=["house", "heart-pulse", "hospital", "book", "robot", "chat-dots", "gear", "box-arrow-right"],
            menu_icon="blank",
            default_index=0
        )

        if selected_menu == "Logout":
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.session_state["page"] = "Login"
            st.rerun()
        else:
            st.session_state["page"] = selected_menu

# ---- Page Routing ----
if st.session_state["page"] == "Login":
    login.show_login_page()
elif st.session_state["page"] == "Signup":
    signup.show_signup_page()
elif st.session_state["page"] == "Home":
    home.show_home_page()
elif st.session_state["page"] == "Check Health":
    check_health.show_check_health_page()
elif st.session_state["page"] == "Doctor Consultation":
    consultation.show_consultation_page()
elif st.session_state["page"] == "Resources":
    resources.show_resources_page()
elif st.session_state["page"]=="Parenting Classes":
    parenting.show_parenting_classes()
elif st.session_state["page"] == "Chatbot":
    chatbot.show_chatbot()
elif st.session_state["page"] == "contactus":
    contactus.show_contact_page()
elif st.session_state["page"] == "Settings":
    settings.show_settings_page()
