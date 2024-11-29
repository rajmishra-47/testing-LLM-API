import streamlit as st

from groq import Groq

client = Groq(
    api_key='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'
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me a recipe with eggs",
        }
    ],
    model="llama3-8b-8192",
)

st.write(chat_completion.choices[0].message.content)
