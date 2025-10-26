import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Study Assistant", page_icon="💬")

# Initialize OpenAI client using Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("💬 AI Study Assistant")
st.write("Ask any question about your studies and get an instant answer.")

# Text input
user_question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if user_question.strip() == "":
        st.warning("Please enter a question first!")
    else:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI study assistant."},
                    {"role": "user", "content": user_question}
                ]
            )
            answer = response.choices[0].message.content
            st.success(answer)
        except Exception as e:
            st.error(f"Error: {e}")
