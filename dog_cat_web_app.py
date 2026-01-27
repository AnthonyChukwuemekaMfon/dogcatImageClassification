import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import cv2

@st.cache_resource # Ensures the model runs only once
# Loading the model
def load_my_model():
    return load_model("pretrained model")
model = load_model("pretrained model")
# Giving the app a title
st.title("Dog VS Cat Image Classification Project")
# Allowing image upload

uploaded_file = st.file_uploader("Upload a cat or a dog image:", type=["jpg", "png", "jpeg"], key="user_input")
if uploaded_file:
    # Convert uploaded file to an image
    img = Image.open(uploaded_file)
    # Displaying the uploaded image
    st.image(img, caption="Uploaded image", use_container_width=True)
    # Resizing the image
    img = img.resize((224, 224))
    # Convert to numpy array
    img = np.asarray(img)
    # Scale the image
    img_scaled = img/255
    # Reshape as an instance
    img_reshape = np.reshape(img_scaled, [1, 224, 224, 3])
    # Making prediction
    img_prediction = model.predict(img_reshape)
    # Converting the predictive result to labels
    img_pred_label = np.argmax(img_prediction)
    # Condition for prediction
    class_names = ["Cat", "Dog"]
    confidence = np.max(img_prediction)
    if confidence < 0.6:
        st.error("❌ This image is neither a clear dog nor a cat. Please upload a valid image!")
    else:
        st.success(f"✅ This is a {class_names[img_pred_label]} image!")

# Resetting the app
# if st.button("🔄Reset"):
#     st.session_state["user_input"] = None
#     st.rerun()
    # if img_pred_label == 0:
    #     st.success("✅This is a **cat** image")
    # elif img_pred_label == 1:
    #     st.success("✅This is a **dog** image")
    # else:
        