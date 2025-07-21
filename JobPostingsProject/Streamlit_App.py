# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 17:13:44 2025

@author: HP
"""

import streamlit as st
import pandas as pd
import joblib

# Load trained model and label encoders
model = joblib.load('job_model.pkl')
le_employment_type = joblib.load('le_employment_type.pkl')
le_location = joblib.load('le_location.pkl')
le_salary = joblib.load('le_salary.pkl')
le_job_title = joblib.load('le_job_title.pkl')

st.title("🕵️‍♂️ Fake Job Posting Detector")

st.write("Enter the details of a job ad to see if it’s likely real or fake.")

# Input form
job_title = st.selectbox("Job Title", le_job_title.classes_)
employment_type = st.selectbox("Employment Type", le_employment_type.classes_)
location = st.selectbox("Location", le_location.classes_)
salary = st.selectbox("Salary", le_salary.classes_)

# Prediction
if st.button("Predict"):
    # Encode inputs
    input_df = pd.DataFrame({
        'employment_type': [le_employment_type.transform([employment_type])[0]],
        'location': [le_location.transform([location])[0]],
        'salary': [le_salary.transform([salary])[0]],
        'job_title': [le_job_title.transform([job_title])[0]]
    })

    # Make prediction
    prediction = model.predict(input_df)[0]
    result = "🟢 This job is likely REAL" if prediction == 0 else "🔴 This job is likely FAKE"

    st.subheader("Prediction Result:")
    st.success(result)