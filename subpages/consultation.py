
import streamlit as st

def show_consultation_page():
    st.title("Doctor Consultation 🩺")

    # Sample list of doctors
    doctors = [
        {
            "name": "Dr. Aditi Sharma",
            "specialization": "Gynecologist & Obstetrician",
            "clinic": "Motherhood Clinic, Mumbai",
            "timings": "Mon-Sat: 10 AM - 5 PM",
            "email": "aditi.sharma@example.com"
        },
        {
            "name": "Dr. Rohan Malhotra",
            "specialization": "Fertility Specialist",
            "clinic": "Wellness Women's Care, Delhi",
            "timings": "Mon-Fri: 9 AM - 3 PM",
            "email": "rohan.malhotra@example.com"
        },
        {
            "name": "Dr. Priya Verma",
            "specialization": "Prenatal Care & Nutrition",
            "clinic": "Healthy Moms Hospital, Bangalore",
            "timings": "Tue-Sat: 11 AM - 6 PM",
            "email": "priya.verma@example.com"
        }
    ]

    # Displaying the doctors in a structured way
    for doctor in doctors:
        with st.expander(f"**{doctor['name']}** ({doctor['specialization']})"):
            st.write(f"📍 **Clinic:** {doctor['clinic']}")
            st.write(f"🕒 **Timings:** {doctor['timings']}")
            st.write(f"📧 **Email:** [{doctor['email']}](mailto:{doctor['email']})")

    st.info("💡 Click on a doctor's name to see more details.")
