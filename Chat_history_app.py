import streamlit as st

# App title
st.title("🤖 Student AI Chat App (Offline Mode)")

# Initialize chat history (only once)
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat input
user_input = st.text_input("Ask something:")

# When user sends a message
if st.button("Send"):
    if user_input:
        # Add user message to history
        st.session_state["messages"].append({"role": "user", "text": user_input})

        # Generate a dummy AI reply (offline)
        ai_reply = f"(🤖 Offline AI): I’m not connected right now, but here’s what I might say about '{user_input}'."
        st.session_state["messages"].append({"role": "ai", "text": ai_reply})
    else:
        st.warning("Please type a message first!")

# Display chat history
st.write("### 💬 Chat History:")
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['text']}")
    else:
        st.markdown(f"**🤖 AI:** {msg['text']}")
