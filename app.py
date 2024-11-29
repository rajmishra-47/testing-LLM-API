import streamlit as st
import os
from groq import Client  # Import the correct class
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key
api_key = os.getenv("GROQ_API_KEY")

# Ensure the API key is loaded
if not api_key:
    raise ValueError("API key not found. Please set GROQ_API_KEY in the .env file.")

# Initialize the client
client = Client(api_key=api_key)

# Make the API call
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me a recipe with eggs",
        }
    ],
    model="llama3-8b-8192",
)

# Output the response
response = chat_completion.choices[0].message.content
st.write(response)
