import streamlit as st
from ultralytics import YOLO
from PIL import Image

model = YOLO("bahraini_food_model.pt")

st.title("🇧🇭 Bahraini Food Classifier")

uploaded_file = st.file_uploader(
    "Upload a Bahraini food image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, use_container_width=True)

    results = model(image)

    probs = results[0].probs

    predicted_class = results[0].names[probs.top1]
    confidence = float(probs.top1conf)

    st.success(f"Prediction: {predicted_class}")
    st.info(f"Confidence: {confidence:.2%}")
