import streamlit as st

def show_cluster2_page():
    st.title("🚨 Quick Doctor Consultation & Intensive Care")
    st.write("This page provides **emergency medical resources, quick doctor consultation options, and intensive care facilities** for high-risk pregnancies.")

    # Quick Doctor Consultation
    st.subheader("🩺 Quick Doctor Consultation")
    st.markdown("- 📞 **Teleconsultation**: Book instant online doctor appointments. [Consult Here](https://www.practo.com/)")
    st.markdown("- 🏥 **Nearby OB-GYN Specialists**: Find the best maternity doctors. [Find Doctors](https://www.zocdoc.com/)")
    st.markdown("- 💬 **24/7 AI Health Chatbot**: Ask health-related queries anytime. [Chat Now](https://www.babylonhealth.com/)")

    # Intensive Maternal Care
    st.subheader("🚑 Intensive Maternal Care")
    st.markdown("- 🚨 **Emergency Maternal Hospitals**: Locate urgent care centers. [Find Nearest Hospitals](https://www.marchofdimes.org/)")
    st.markdown("- 🏥 **NICU & ICU for High-Risk Pregnancies**: Specialized care for complicated pregnancies. [Read More](https://www.mayoclinic.org/tests-procedures/nicu/about/pac-20394919)")
    st.markdown("- 👶 **Premature Birth Support**: Special assistance for preterm births. [Support Guide](https://www.marchofdimes.org/find-support)")

    # Additional Emergency Support
    st.subheader("📢 Emergency Contacts")
    st.markdown("- 🚑 **Ambulance Services**: Dial 911 or [Find Nearest Services](https://www.emergencycareforyou.org/)")
    st.markdown("- 📞 **Maternal Helplines**: Government & NGO support for maternal health crises.")

