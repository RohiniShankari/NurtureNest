import os

api_key = os.getenv("GOOGLE_API_KEY", "AIzaSyAMejN6ZgG7ptXc6rUHLSYzV2_UJTfbw0w")  # Replace with your actual key
import google.generativeai as genai

genai.configure(api_key=api_key)  # Replace with your valid key

def test_gemini():
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Use a valid model
        response = model.generate_content("Hello Gemini!")
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

test_gemini()
