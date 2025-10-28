import streamlit as st

st.set_page_config(page_title="Upload Photos", page_icon="📸", layout="centered")

st.title("📸 Upload Your Photos")

st.write("Share your study setup, notes, or any photo you want!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Text input for caption or message
caption = st.text_area("✍️ Write something about your photo:", placeholder="Type here...")

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Your uploaded photo", use_column_width=True)

    if caption:
        st.success("✅ Photo and message uploaded successfully!")
        st.write(f"📝 **Your message:** {caption}")

        # Optional: save image + caption offline
        with open(f"uploaded_{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())

        with open("captions.txt", "a") as f:
            f.write(f"{uploaded_file.name}: {caption}\n")

else:
    st.info("👆 Upload a photo to get started!")
