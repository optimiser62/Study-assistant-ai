import streamlit as st

st.title("📸 Upload Your Photos")

st.write("Share your study setup, notes, or any photo you want!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show uploaded image
    st.image(uploaded_file, caption="Your uploaded photo", use_column_width=True)

    # Optional: Save image to folder (for offline apps)
    with open(f"uploaded_{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✅ Photo saved successfully!")
