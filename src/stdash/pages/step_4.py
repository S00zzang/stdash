import streamlit as st
from PIL import Image
from transformers import pipeline
import io
import random

st.markdown("# STEP 4 ❤")
st.sidebar.markdown("# STEP 4 ❤")

st.title(':hotdog:핫도그 판별기')

# Load the model
model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")

# Streamlit app layout
st.write("핫도그세요?")

# Upload file
uploaded_file = st.file_uploader("사진 좀 보여주세요...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read and process the image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Make prediction
    p = model(img)

    # Get prediction label
    score = p[0]['score']

    # Display result
    if score < 0.8:
        st.warning("당신.. 핫도그 아니지..누구야..")
        dog = "https://github.com/user-attachments/assets/6fe35248-d638-4bf0-8194-74de04c7d496"
        st.image(dog, use_column_width=True)
    else:
        st.success("아~ 핫도그셨구나! 반가워요!")
        hotdog = "https://github.com/user-attachments/assets/a12bac57-61b3-47a8-b8fe-0751461e5839"
        st.image(hotdog, use_column_width=True)

