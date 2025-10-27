import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# App title and layout
st.set_page_config(page_title="AI Study Assistant", page_icon="🎓", layout="centered")
st.title("🎓 AI Study Assistant")
st.caption("Your friendly AI helper for quick study answers!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display past chat messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your question...")

if user_input:
    # Save user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state["messages"]
            )
            answer = response.choices[0].message.content
            message_placeholder.markdown(answer)
            st.session_state["messages"].append({"role": "assistant", "content": answer})
        except Exception as e:
            message_placeholder.error("⚠️ Error: Please check your API key or quota.")
