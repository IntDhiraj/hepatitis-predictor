# import streamlit as st
# import pandas as pd
# import joblib

# # Load trained model
# model = joblib.load("hepatitis_model.pkl")

# # Title
# st.title("Hepatitis Disease Prediction")

# st.write("Enter patient details below:")

# # Inputs
# age = st.number_input("Age", 0, 100)

# bilirubin = st.number_input(
#     "Bilirubin",
#     min_value=0.0,
#     step=0.1
# )

# albumin = st.number_input(
#     "Albumin",
#     min_value=0.0,
#     step=0.1
# )

# ascites = st.selectbox(
#     "Ascites",
#     [0, 1]
# )

# spiders = st.selectbox(
#     "Spiders",
#     [0, 1]
# )

# sgot = st.number_input(
#     "SGOT",
#     min_value=0.0,
#     step=1.0
# )

# alk_phosphate = st.number_input(
#     "Alk Phosphate",
#     min_value=0.0,
#     step=1.0
# )

# # Prediction button
# if st.button("Predict"):

#     input_data = pd.DataFrame([[
#         bilirubin,
#         albumin,
#         ascites,
#         spiders,
#         sgot,
#         age,
#         alk_phosphate
#     ]], columns=[
#         'bilirubin',
#         'albumin',
#         'ascites',
#         'spiders',
#         'sgot',
#         'age',
#         'alk_phosphate'
#     ])

#     # Prediction
#     prediction = model.predict(input_data)

#     # Output
#     if prediction[0] == 1:
#         st.success("Prediction: Patient will LIVE")
#     else:
#         st.error("Prediction: Patient will DIE")

import streamlit as st
import pandas as pd
import joblib

# Page settings
st.set_page_config(
    page_title="Hepatitis Predictor",
    page_icon="🩺",
    layout="centered"
)

# Load model
model = joblib.load("hepatitis_model.pkl")

# Custom CSS
st.markdown("""
<style>

/* Animated background */
.stApp {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #000000);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    color: white;
}

@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

/* Fade animation */
.fade-in {
    animation: fadeIn 1.5s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* Card style */
.main-card {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
    margin-top: 20px;
}

/* Welcome section */
.welcome-box {
    text-align: center;
    padding-top: 100px;
}

.welcome-title {
    font-size: 45px;
    font-weight: bold;
    color: white;
}

.welcome-sub {
    font-size: 18px;
    color: #d1d1d1;
    margin-top: 10px;
    margin-bottom: 30px;
}

/* Button style */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 25px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px #00c6ff;
}

</style>
""", unsafe_allow_html=True)

# Session state
if "start" not in st.session_state:
    st.session_state.start = False

# Welcome page
if not st.session_state.start:

    st.markdown("""
    <div class='welcome-box fade-in'>
        <div class='welcome-title'>
            🩺 Hepatitis Prediction System
        </div>

        <div class='welcome-sub'>
            AI Powered Disease Prediction Web Application
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    if st.button("Continue to Predict"):
        st.session_state.start = True
        st.rerun()

# Prediction page
else:

    st.markdown("<div class='main-card fade-in'>", unsafe_allow_html=True)

    st.title("🧬 Hepatitis Disease Prediction")

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

    # Predict button
    if st.button("Predict Result"):

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

        prediction = model.predict(input_data)

        st.write("")

        if prediction[0] == 1:
            st.success("✅ Prediction: Patient will LIVE")
        else:
            st.error("⚠️ Prediction: Patient may DIE")

    st.markdown("</div>", unsafe_allow_html=True)