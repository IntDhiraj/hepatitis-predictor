import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("hepatitis_model.pkl")

# Title
st.title("Hepatitis Disease Prediction")

st.write("Enter patient details below:")

# Inputs
age = st.number_input("Age", 0, 100)

bilirubin = st.number_input(
    "Bilirubin",
    min_value=0.0,
    step=0.1
)

albumin = st.number_input(
    "Albumin",
    min_value=0.0,
    step=0.1
)

ascites = st.selectbox(
    "Ascites",
    [0, 1]
)

spiders = st.selectbox(
    "Spiders",
    [0, 1]
)

sgot = st.number_input(
    "SGOT",
    min_value=0.0,
    step=1.0
)

alk_phosphate = st.number_input(
    "Alk Phosphate",
    min_value=0.0,
    step=1.0
)

# Prediction button
if st.button("Predict"):

    input_data = pd.DataFrame([[
        bilirubin,
        albumin,
        ascites,
        spiders,
        sgot,
        age,
        alk_phosphate
    ]], columns=[
        'bilirubin',
        'albumin',
        'ascites',
        'spiders',
        'sgot',
        'age',
        'alk_phosphate'
    ])

    # Prediction
    prediction = model.predict(input_data)

    # Output
    if prediction[0] == 1:
        st.success("Prediction: Patient will LIVE")
    else:
        st.error("Prediction: Patient will DIE")