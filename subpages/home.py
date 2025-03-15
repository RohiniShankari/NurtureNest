       
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Replace with your image URL or local path
image_path = "./image.jpeg" # Changed to image_path to reflect a local file

def load_local_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        st.error(f"Error: Image not found at {image_path}")
        return None
    except Exception as e:
        st.error(f"Unexpected error loading image: {e}")
        return None

def show_home_page():
    st.title("Welcome to NurtureNest")
    st.subheader("a maternal health and wellness app")

    # Create two columns
    col1, col2 = st.columns([1, 1])  # Equal width columns

    # Load and display the image in the first column
    with col1:
        image = load_local_image(image_path) #changed to load_local_image
        if image:
            st.image(image, use_container_width=True)

    # Display text in the second column
    with col2:
        st.subheader("Your Personalized Pregnancy Companion")
        st.write("""
            This app is designed to provide personalized health recommendations for pregnant women.
            You can check your health status, consult a doctor, and explore valuable health resources.
        """)

        st.subheader("Key Features")
        st.write("""
            * **Health Tracking:** Monitor your symptoms and progress.
            * **Doctor Consultations:** Connect with healthcare professionals.
            * **Resource Library:** Access expert articles and information.
            * **Personalized Recommendations:** Receive tailored advice.
        """)
