import streamlit as st
import openai

st.title("AI Study Assistant 🤖")

# Ask user for a question
user_input = st.text_input("Ask me anything:")

# Load your OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful and knowledgeable AI study assistant who gives clear, educational answers to students."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.write(response["choices"][0]["message"]["content"])
        except Exception as e:
            st.error(f"Error: {e}")
