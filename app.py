import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Load model
model = tf.keras.models.load_model('./model/cat_model.h5')
class_names = ["Abyssinian", "Bengal", "Bombay", "British Shorthair", 
                "Domestic", "Maine Coon", "Persian", "Ragdoll", 
                "Siamese", "Sphynx"]
class_descriptions = {
    "Abyssinian": "Ini jenis kucing Abyssinian",
    "Bengal": "Ini jenis kucing Bengal",
    "Bombay": "Ini jenis kucing Bombay",
    "British Shorthair": "Ini jenis kucing British Shorthair",
    "Domestic": "Ini jenis kucing Domestic",
    "Maine Coon": "Ini jenis Maine Coon",
    "Persian": "Ini jenis kucing Persian",
    "Ragdoll": "Ini jenis kucing Ragdoll",
    "Siamese": "Ini jenis kucing Siamese",
    "Sphynx": "Ini jenis kucing Sphynx"
}

# CSS Styling
st.markdown("""
    <style>
        .title {
            font-size: 2.5em;
            color: #F3F3E0;
            text-align: center;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .result-box {
            background-color: #F4F6FF;
            padding: 20px;
            border-radius: 10px;
            border: 2px solid #d3d3d3;
            text-align: center;
            margin-top: 20px;
        }
        .prediction {
            font-size: 1.5em;
            font-weight: bold;
            color: #133E87; 
        }
        .confidence {
            font-size: 1.25em;
            font-weight: bold;
            color: #4682B4; 
        }
        .warning {
            font-size: 1.25em;
            color: #FF6347;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<h1 class='title'>Cat Image Classifier 🐈‍⬛😻🐈</h1>
<p style='font-size: 16px; color: #F3F3E0; text-align: center'>This application is a Cat image classifier designed to predict the type of Cat in a given image. Upload or capture an image, and our model will analyze it to determine the most likely category, providing a confidence score along with a brief description of the result.</p>
""", unsafe_allow_html=True)


# Prediction function
def predict(image):
    if image.mode != 'RGB':
        image = image.convert("RGB")
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence_score = np.max(predictions) * 100
    return predicted_class, confidence_score

# Input method selection
input_method = st.selectbox("Pilih metode input foto:", ["Upload Foto", "Ambil Foto"])

# Set confidence threshold
confidence_threshold = 85.0

# Upload photo functionality
if input_method == "Upload Foto":
    uploaded_image = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        predicted_class, confidence_score = predict(image)
        
        # Check confidence score
        if confidence_score < confidence_threshold:
            st.markdown(f"<div class='result-box'><p class='warning'>Foto ini kemungkinan bukan foto kucing, coba foto yang lainnya.</p></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='result-box'><h3 class='prediction'>Prediksi: {class_descriptions[predicted_class]}</h3><p class='confidence'>Confidence Score: {confidence_score:.2f}%</p></div>", unsafe_allow_html=True)

# Capture photo functionality
elif input_method == "Ambil Foto":
    captured_image = st.camera_input("Take a photo")
    if captured_image:
        image = Image.open(captured_image)
        st.image(image, caption="Captured Image", use_column_width=True)
        
        predicted_class, confidence_score = predict(image)
        
        # Check confidence score
        if confidence_score < confidence_threshold:
            st.markdown(f"<div class='result-box'><p class='warning'>Foto ini kemungkinan bukan foto kucing, coba foto yang lainnya.</p></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='result-box'><h3 class='prediction'>Prediksi: {class_descriptions[predicted_class]}</h3><p class='confidence'>Confidence Score: {confidence_score:.2f}%</p></div>", unsafe_allow_html=True)
