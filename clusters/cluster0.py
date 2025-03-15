import streamlit as st

def show_resources_cluster_0():
    st.title("🧘‍♀️ Yoga & Dietary Resources for Maternal Health (Cluster 0)")

    # Yoga Section
    st.header("🧘‍♀️ Recommended Yoga Poses for Pregnancy")
    st.write("""
    Practicing yoga during pregnancy can help with flexibility, relaxation, and reducing stress. Here are some safe and beneficial poses:
    """)

    yoga_poses = {
        "1. Cat-Cow Stretch (Marjaryasana-Bitilasana)": "Improves spinal flexibility and relieves back pain.",
        "2. Butterfly Pose (Baddha Konasana)": "Helps open up the hips and strengthens pelvic muscles.",
        "3. Side Stretch (Parsva Urdhva Hastasana)": "Reduces back pain and improves blood circulation.",
        "4. Seated Forward Bend (Paschimottanasana - modified)": "Enhances digestion and calms the nervous system.",
        "5. Pelvic Tilts": "Strengthens the lower back and prepares for labor."
    }

    for pose, benefit in yoga_poses.items():
        st.subheader(pose)
        st.write(benefit)

    st.info("⚠️ Always consult your doctor before starting any exercise routine during pregnancy.")

    # Dietary Recommendations
    st.header("🥗 Nutrition & Diet for Pregnant Women (Cluster 0)")
    st.write("""
    A healthy diet is crucial for both mother and baby's growth. Here are some essential dietary tips:
    """)

    dietary_tips = [
        "✅ **Protein-rich foods**: Lentils, eggs, fish, lean meat, and dairy products.",
        "✅ **Iron sources**: Green leafy vegetables, fortified cereals, and lean meats.",
        "✅ **Calcium-rich foods**: Milk, yogurt, cheese, almonds, and tofu.",
        "✅ **Folic Acid intake**: Spinach, broccoli, beans, and fortified grains to prevent birth defects.",
        "✅ **Hydration**: Drink at least 8-10 glasses of water daily.",
        "✅ **Healthy Fats**: Avocados, nuts, and olive oil for brain development.",
        "✅ **Fiber-rich foods**: Whole grains, fruits, and vegetables to prevent constipation."
    ]

    for tip in dietary_tips:
        st.write(tip)

    st.warning("⚠️ Avoid raw seafood, unpasteurized dairy, excessive caffeine, and processed foods.")

