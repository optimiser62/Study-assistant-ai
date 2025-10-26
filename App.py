import streamlit as st
from openai import OpenAI

st.title("💬 AI Study Assistant")

# Create OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
if prompt := st.chat_input("Ask your study question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Get AI answer
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and smart AI study assistant."},
                *st.session_state.messages
            ]
        )
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
