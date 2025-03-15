import streamlit as st
from clusters import cluster0,cluster1,cluster2

def show_resources_page():
    st.title("📚 Maternal Health Resources")

    # Select Cluster
    selected_cluster = st.selectbox("🩺 Choose Your Health Cluster", [0, 1, 2])

    # Navigate to the corresponding cluster page
    if selected_cluster == 0:
        cluster0.show_resources_cluster_0()  # Calls function from cluster0.py
    elif selected_cluster == 1:
        cluster1.show_cluster1_page()  # Calls function from cluster1.py
    elif selected_cluster == 2:
        cluster2.show_cluster2_page()  # Calls function from cluster2.py


