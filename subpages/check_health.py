import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load models
with open("hc_model.pkl", "rb") as model_file:
    hc_model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

with open("cluster_centroids.pkl", "rb") as centroids_file:
    cluster_centroids = pickle.load(centroids_file)

# Recommendations
recommendations = {
    0: "Maintain a healthy lifestyle with regular exercise and a balanced diet.",
    1: "Monitor blood pressure & sugar levels. Reduce salt & sugar intake.",
    2: "High risk detected! Consult a doctor immediately for detailed screening."
}

def predict_cluster(user_data):
    user_data = np.array(user_data).reshape(1, -1)
    user_data_df = pd.DataFrame(user_data, columns=scaler.feature_names_in_)
    user_data_scaled = scaler.transform(user_data_df)
    distances = np.linalg.norm(cluster_centroids.values - user_data_scaled, axis=1)
    return np.argmin(distances)

def show_check_health_page():
    st.title("Check Your Health 🩺")

    age = st.number_input("Age", min_value=10, max_value=100, value=30)
    systolic_bp = st.number_input("Systolic BP", min_value=80, max_value=200, value=120)
    diastolic_bp = st.number_input("Diastolic BP", min_value=50, max_value=150, value=80)
    bs = st.number_input("Blood Sugar Level", min_value=3.0, max_value=15.0, value=5.5)
    body_temp = st.number_input("Body Temperature (°F)", min_value=95.0, max_value=105.0, value=98.6)
    heart_rate = st.number_input("Heart Rate (BPM)", min_value=40, max_value=150, value=75)

    if st.button("Get Health Recommendation"):
        user_input = [age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]
        predicted_cluster = predict_cluster(user_input)
        recommendation = recommendations.get(predicted_cluster, "No recommendation available.")

        st.subheader("Predicted Health Risk Cluster:")
        st.write(f"You belong to **Cluster {predicted_cluster}**")

        st.subheader("Health Recommendation:")
        st.write(recommendation)
