import streamlit as st
from PIL import Image

# Dummy model (replace with real model later)
def dummy_predict(img):
    return "Pizza", "285 kcal"

# Set page config
st.set_page_config(page_title="Food Calorie Estimator", layout="centered", page_icon="🍕")

# Beautiful custom CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #f9f9f9, #e0f7fa);
        font-family: 'Segoe UI', sans-serif;
    }

    .stApp {
        background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
        background-size: cover;
    }

    .title {
        text-align: center;
        font-size: 2.8em;
        font-weight: bold;
        color: #2E3B55;
        margin-bottom: 0.2em;
    }

    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #616161;
        margin-bottom: 1.5em;
    }

    .upload-box {
        background-color: #ffffffcc;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        text-align: center;
    }

    .result-box {
        background-color: #fff8e1;
        border-left: 5px solid #ff9800;
        padding: 15px;
        border-radius: 12px;
        margin-top: 1.5em;
        font-size: 18px;
    }

    .stButton>button {
        background-color: #43a047;
        color: white;
        padding: 0.5em 1.2em;
        font-size: 16px;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #388e3c;
    }
    </style>
""", unsafe_allow_html=True)

# Title + subtitle
st.markdown('<div class="title">🍽️ AI Food Calorie Estimator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload a food image and get calorie estimation instantly</div>', unsafe_allow_html=True)

# Upload section
with st.container():
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("📷 Upload a food image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            if st.button("🔥 Estimate Calories"):
                food, calories = dummy_predict(image)
                st.markdown(f"""
                    <div class="result-box">
                        🍱 <strong>Food Detected:</strong> {food}<br>
                        🔥 <strong>Calories:</strong> {calories}
                    </div>
                """, unsafe_allow_html=True)

        except:
            st.error("❌ Invalid image. Please try another one.")
    st.markdown('</div>', unsafe_allow_html=True)

