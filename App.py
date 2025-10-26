import streamlit as st
from openai import OpenAI

# Page title
st.title("💬 AI Study Assistant")

# Create OpenAI client (uses your Streamlit secret key)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# User input box
question = st.text_input("Ask me anything related to your studies:")

if question:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful, smart AI study assistant for students. Explain answers clearly and simply."},
                    {"role": "user", "content": question}
                ]
            )
            # Display the AI's reply
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
