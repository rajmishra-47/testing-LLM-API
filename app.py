import streamlit as st
from groq import Client

# Access the API key from Streamlit secrets
api_key = st.secrets["GROQ"]["GROQ_API_KEY"]

# Initialize the Groq client with the API key
client = Client(api_key=api_key)

# Use the client for your API calls (example below)
chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "Tell me a recipe with eggs"}],
    model="llama3-8b-8192",
)

# Display the response
st.write(chat_completion.choices[0].message.content)
