import streamlit as st
from openai import OpenAI

# Get API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("💬 AI Study Assistant")

prompt = st.text_input("Ask me anything about your studies:")

if st.button("Get Answer"):
    if prompt:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI study assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a question first!")
