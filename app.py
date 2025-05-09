import streamlit as st
import pandas as pd
from joblib import load
import xgboost
from xgboost import XGBClassifier


# Load the trained model and scaler
model = load('xgb_model.joblib')            
scaler = load('robust_scaler.joblib')       

# App title and description
st.title("Heart Failure Prediction")
st.markdown("Predict the likelihood of heart failure based on key clinical features.")

# Input form
time = st.number_input("Follow-up Period (days)", min_value=0, step=1)
ejection_fraction = st.number_input("Ejection Fraction (%)", min_value=0, max_value=100, step=1)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.0, step=0.1)

# On click
if st.button("Predict"):
    # Prepare input
    input_data = pd.DataFrame({
        'time': [time],
        'ejection_fraction': [ejection_fraction],
        'serum_creatinine': [serum_creatinine]
    })

    # Apply scaling
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    result = "⚠️ High Risk of Heart Failure" if prediction[0] == 1 else "✅ Low Risk of Heart Failure"
    st.success(f"Prediction: {result}")
