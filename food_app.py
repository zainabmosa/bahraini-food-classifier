import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.set_page_config(page_title="Bahraini Food AI", page_icon="🇧🇭", layout="wide", initial_sidebar_state="expanded")

st.markdown("""<style>.main{background-color:#faf9f6}.hero{padding:2rem 2rem 1.5rem 2rem;border-radius:25px;background:linear-gradient(135deg,#7a1f2b,#b84c5a);color:white;text-align:center;margin-bottom:2rem}.hero h1{font-size:3rem;margin-bottom:.3rem}.hero p{font-size:1.15rem;margin-top:0}.prediction-card{padding:1.5rem;border-radius:20px;background:white;border:1px solid #eeeeee;box-shadow:0 4px 15px rgba(0,0,0,.06);text-align:center;margin-top:1rem}.prediction-name{font-size:2rem;font-weight:700;margin:.5rem 0;text-transform:capitalize}.confidence{font-size:1.2rem;margin-bottom:.5rem}.food-card{padding:1rem;border-radius:15px;background:white;border:1px solid #eeeeee;text-align:center;margin-bottom:.7rem}.section-title{font-size:1.5rem;font-weight:700;margin-top:1rem;margin-bottom:1rem}.footer{text-align:center;padding:2rem 0 1rem 0;color:#777;font-size:.9rem}</style>""", unsafe_allow_html=True)

DISPLAY_NAMES = {"balalet":"Balaleet","halwa":"Halwa","karak":"Karak","luqemat":"Luqaimat","makboos":"Machboos","raqaQ":"Raqaq","raqaq":"Raqaq","sambosa":"Samboosa","teka":"Tikka"}

@st.cache_resource
def load_model():
    return YOLO("bahraini_food_model.pt")

model = load_model()

with st.sidebar:
    st.title("🇧🇭 Bahrain Food AI")
    st.markdown("---")
    st.markdown("### 🍽️ Supported Foods")
    foods = ["Balaleet","Halwa","Karak","Luqaimat","Machboos","Raqaq","Samboosa","Tikka"]
    for food in foods:
        st.write(f"• {food}")
    st.markdown("---")
    st.markdown("### 🤖 About the Model")
    st.write("This application uses a YOLO-based image classification model trained to recognize traditional Bahraini foods.")
    st.markdown("---")
    st.caption("🇧🇭 Bahraini Food AI • Machine Learning Project")

st.markdown("""<div class="hero"><h1>🇧🇭 Bahraini Food AI</h1><p>Discover the Bahraini dish in your photo using Artificial Intelligence</p></div>""", unsafe_allow_html=True)

st.markdown("### 📸 Upload a Food Image")
st.write("Upload a clear photo of a Bahraini food item and let the AI identify it.")

input_method = st.radio("Choose input method:", ["📷 Take a Photo", "🖼️ Upload an Image"], horizontal=True)

if input_method == "📷 Take a Photo":
    uploaded_file = st.camera_input("Take a photo of your Bahraini food")
else:
    uploaded_file = st.file_uploader("Choose an image", type=["jpg","jpeg","png"], label_visibility="collapsed")
    
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    col1, col2 = st.columns([1.15,1])
    with col1:
        st.markdown("### 🖼️ Your Image")
        st.image(image, use_container_width=True)
    with col2:
        st.markdown("### 🤖 AI Prediction")
        with st.spinner("AI is analyzing your food... 🍽️"):
            results = model(image, verbose=False)
        probs = results[0].probs
        predicted_id = int(probs.top1)
        predicted_class = results[0].names[predicted_id]
        display_class = DISPLAY_NAMES.get(predicted_class, predicted_class.title())
        confidence = float(probs.top1conf)
        st.markdown(f"""<div class="prediction-card"><div>🏆 Most Likely Dish</div><div class="prediction-name">{display_class}</div><div class="confidence">Confidence: <b>{confidence:.2%}</b></div></div>""", unsafe_allow_html=True)
        st.progress(confidence, text=f"AI Confidence: {confidence:.1%}")
        st.markdown("### 📊 Top Predictions")
        probabilities = probs.data.cpu().numpy()
        top_indices = probabilities.argsort()[::-1][:3]
        for index in top_indices:
            probability = float(probabilities[index])
            class_name = results[0].names[int(index)]
            display_name = DISPLAY_NAMES.get(class_name, class_name.title())
            percentage = probability * 100
            st.write(f"**{display_name}** — {percentage:.2f}%")
            st.progress(probability, text=f"{percentage:.1f}%")
else:
    st.markdown("---")
    st.markdown('<div class="section-title">🍴 Explore Bahraini Cuisine</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    food_info = [("🍜","Balaleet"),("🍮","Halwa"),("☕","Karak"),("🍚","Machboos"),("🥟","Samboosa"),("🍯","Luqaimat"),("🥞","Raqaq"),("🍽️","Tikka")]
    columns = [col1,col2,col3,col4]
    for i,(emoji,name) in enumerate(food_info):
        with columns[i % 4]:
            st.markdown(f"""<div class="food-card"><div style="font-size:2rem;">{emoji}</div><b>{name}</b></div>""", unsafe_allow_html=True)

st.markdown("""<div class="footer">🇧🇭 Made with AI • Bahraini Food Classification<br>Traditional food • Machine Learning • Computer Vision</div>""", unsafe_allow_html=True)
