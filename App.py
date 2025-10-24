# Install dependencies first:
# pip install streamlit openai

import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

st.title("Study Q&A Assistant 📚")
st.write("Ask any study-related question and get a direct answer!")

# Input from user
question = st.text_input("Enter your question:")

if st.button("Get Answer") and question:
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-5-mini",
                messages=[
                    {"role": "system",
