import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="AI Study Assistant 🤖", page_icon="📘")
st.title("📘 AI Study Assistant")
st.write("Welcome! I'm your AI-powered study helper. Ask me any study question below 👇")

if "chat" not in st.session_state:
    st.session_state.chat = []

def generate_response(question):
    responses = [
        "That's an interesting question! Let's think about it logically.",
        "Hmm… that’s related to one of your study topics.",
        "Try focusing on the key concept behind that topic.",
        "Good question! Maybe review your notes on that.",
        "You’re doing great — keep exploring such ideas!"
    ]
    return random.choice(responses)

user_input = st.text_input("💬 Type your question:")

if user_input:
    response = generate_response(user_input)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Assistant", response))

for role, text in st.session_state.chat:
    if role == "You":
        st.markdown(f"**🧑‍🎓 You:** {text}")
    else:
        st.markdown(f"**🤖 Assistant:** {text}")
