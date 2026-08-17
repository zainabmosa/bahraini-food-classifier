import streamlit as st
from ultralytics import YOLO
from PIL import Image
import json

st.set_page_config(page_title="Bahraini Food Classifier",page_icon="🍽️")

st.title("🇧🇭 Bahraini Food Classifier")
st.write("Upload an image of Bahraini food and the model will predict the food type.")

@st.cache_resource
def load_model():
    return YOLO("bahraini_food_model.pt")

model = load_model()

with open("class_names.json", "r") as f:
    class_names = json.load(f)

uploaded_file = st.file_uploader("Upload a food image",type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image,caption="Uploaded Image",use_container_width=True)

    results = model(image)

    probs = results[0].probs

    predicted_id = int(probs.top1)
    confidence = float(probs.top1conf)

    predicted_class = class_names[str(predicted_id)]

    st.success(f"Prediction: {predicted_class}")
    st.info(f"Confidence: {confidence:.2%}")