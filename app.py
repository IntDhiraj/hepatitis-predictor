import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("hepatitis_model.pkl")

st.title("Hepatitis B Disease Prediction")

st.write("Enter patient details below:")

# User Inputs
age = st.number_input("Age", 0, 100)
sex = st.selectbox("Sex", ["Female", "Male"])
steroid = st.selectbox("Steroid", [0, 1])
antivirals = st.selectbox("Antivirals", [0, 1])
fatigue = st.selectbox("Fatigue", [0, 1])
malaise = st.selectbox("Malaise", [0, 1])
anorexia = st.selectbox("Anorexia", [0, 1])
liver_big = st.selectbox("Liver Big", [0, 1])
liver_firm = st.selectbox("Liver Firm", [0, 1])
spleen_palpable = st.selectbox("Spleen Palpable", [0, 1])
spiders = st.selectbox("Spiders", [0, 1])
ascites = st.selectbox("Ascites", [0, 1])
varices = st.selectbox("Varices", [0, 1])

bilirubin = st.number_input("Bilirubin")
alk_phosphate = st.number_input("Alk Phosphate")
sgot = st.number_input("SGOT")
albumin = st.number_input("Albumin")
protime = st.number_input("Protime")
histology = st.selectbox("Histology", [0, 1])

# Convert sex to encoded value
if sex == "Male":
    sex = 1
else:
    sex = 0

# Prediction button
if st.button("Predict"):

    input_data = [[
        age,
        sex,
        steroid,
        antivirals,
        fatigue,
        malaise,
        anorexia,
        liver_big,
        liver_firm,
        spleen_palpable,
        spiders,
        ascites,
        varices,
        bilirubin,
        alk_phosphate,
        sgot,
        albumin,
        protime,
        histology
    ]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Prediction: Patient will LIVE")
    else:
        st.error("Prediction: Patient will DIE")