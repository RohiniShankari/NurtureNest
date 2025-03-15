import streamlit as st


import google.generativeai as genai
#api_key="AIzaSyAMejN6ZgG7ptXc6rUHLSYzV2_UJTfbw0w"
api_key="AIzaSyB-rsrWbHN4ZPTFQyvt48y3qu0_r2K1AaY"

genai.configure(api_key=api_key)

def show_chatbot():
    st.title("💬 AI Chatbot")

    user_input = "considering the maternal health"+st.text_input("Ask me anything:")
    if st.button("Submit"):
        if user_input:
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            response = model.generate_content(user_input)
            st.write("🤖 Gemini:", response.text)
        else:
            st.warning("Please enter a question!")
