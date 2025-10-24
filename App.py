import streamlit as st
import openai

st.title("AI Study Assistant 🤖")

# Ask for user input
user_input = st.text_input("Ask me anything:")

# Check if API key is set in Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI study assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.write(response["choices"][0]["message"]["content"])
        except Exception as e:
            st.error(f"Error: {e}")
