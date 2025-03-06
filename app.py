import streamlit as st
import pickle
import pandas as pd

# Load the trained model and feature names
with open("rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)
    model = model_data["model"]
    feature_names = model_data["feature_names"]

# Apply custom CSS for background image and styling
st.markdown(
    """
    <style>
        body {
            background-image: url('https://source.unsplash.com/1600x900/?rain');
            background-size: cover;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background: rgba(0, 0, 0, 0.6);
            padding: 20px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.markdown("<h1 style='text-align: center; color: cyan;'>Rainfall Prediction App</h1>", unsafe_allow_html=True)
st.write("### Enter the weather conditions to predict whether it will rain or not.")

# Create input fields for user input
inputs = []
for feature in feature_names:
    value = st.number_input(f"Enter {feature}", value=0.0)
    inputs.append(value)

# Convert inputs to DataFrame
input_df = pd.DataFrame([inputs], columns=feature_names)

# Prediction button
if st.button("Predict", key="predict_button"):
    prediction = model.predict(input_df)
    result = "🌧️ Rainfall Expected" if prediction[0] == 1 else "☀️ No Rainfall"
    st.markdown(f"<h2 style='text-align: center; color: yellow;'>{result}</h2>", unsafe_allow_html=True)
