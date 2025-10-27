import streamlit as st

st.set_page_config(page_title="AI Study Assistant", page_icon="💬", layout="centered")

# --- Custom CSS for chat style ---
st.markdown("""
    <style>
        .chat-container {
            max-height: 450px;
            overflow-y: auto;
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
        .user-bubble {
            background-color: #DCF8C6;
            color: black;
            padding: 10px 14px;
            border-radius: 15px;
            margin: 5px 0;
            text-align: right;
            max-width: 75%;
            float: right;
            clear: both;
        }
        .bot-bubble {
            background-color: #E5E5EA;
            color: black;
            padding: 10px 14px;
            border-radius: 15px;
            margin: 5px 0;
            text-align: left;
            max-width: 75%;
            float: left;
            clear: both;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("💬 AI Study Assistant")
st.write("Your friendly AI helper for quick study answers!")

# --- Chat history storage ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Display previous chats ---
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f'<div class="user-bubble">{chat["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">{chat["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Input area ---
user_input = st.text_input("Type your question:", placeholder="e.g. What is photosynthesis?")

if st.button("Ask"):
    if user_input.strip() != "":
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        # Simple AI response (offline placeholder)
        bot_reply = "I'm still learning, but here's what I found about that topic!"
        st.session_state.chat_history.append({"role": "bot", "content": bot_reply})
        st.experimental_rerun()

# --- Clear chat ---
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()
