import streamlit as st

st.title("My AI App 🚀")

question = st.text_input("Ask me anything:")

if question:
    st.write("Good question! I'm still learning to answer — update coming soon 🔧")
else:
    st.write("Type a question above to start.")
