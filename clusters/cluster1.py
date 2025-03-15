import streamlit as st

def show_cluster1_page():
    st.title("⚠️ Managing Blood Pressure & Sugar")
    st.write("This page provides resources for managing high blood pressure, diabetes, and extra maternal care.")

    # Blood Pressure & Sugar Management Section
    st.subheader("🩺 Managing Blood Pressure & Sugar")
    st.markdown("- 🩸 **Track Your BP & Sugar Levels**: Regular monitoring is essential. [Guide](https://www.heart.org/en/health-topics/high-blood-pressure/changes-you-can-make-to-manage-high-blood-pressure)")
    st.markdown("- 🍏 **Healthy Diet**: Reduce salt, sugar, and processed food intake. [Diet Plan](https://www.diabetes.org/healthy-living/recipes-nutrition)")
    st.markdown("- 🏃‍♀️ **Exercise Routine**: Light exercise like walking & prenatal yoga can help. [Prenatal Workouts](https://www.youtube.com/watch?v=d-J1KUp5nho)")

    # Extra Care Section
    st.subheader("🚨 Extra Maternal Care")
    st.markdown("- 🤰 **Specialized Doctor Consultation**: Get expert medical advice. [Find Doctors](https://www.zocdoc.com/)")
    st.markdown("- 🏥 **Emergency Maternal Hospitals**: Locate nearby maternal care centers. [Find Hospitals](https://www.marchofdimes.org/)")
    st.markdown("- 🧘‍♀️ **Mental Health Support**: Managing stress is crucial. [Guidance](https://www.womenshealth.gov/mental-health)")

