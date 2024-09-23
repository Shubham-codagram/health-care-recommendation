import streamlit as st
import pandas as pd

# Sample symptoms and corresponding conditions (for demonstration purposes)
SYMPTOM_CONDITIONS = {
    "Fever": ["Flu", "COVID-19", "Infection"],
    "Cough": ["Cold", "Allergy", "COVID-19"],
    "Fatigue": ["Anemia", "Thyroid issues", "Depression"],
    "Headache": ["Migraine", "Tension headache", "Dehydration"],
    "Nausea": ["Food poisoning", "Gastritis", "Pregnancy"],
}

# Function to check symptoms
def check_symptoms(symptoms):
    conditions = []
    for symptom in symptoms:
        if symptom in SYMPTOM_CONDITIONS:
            conditions.extend(SYMPTOM_CONDITIONS[symptom])
    return set(conditions)  # Return unique conditions

# Streamlit interface
st.title("Symptom Checker")

# User input for symptoms
st.subheader("Select your symptoms")
selected_symptoms = st.multiselect("Symptoms", list(SYMPTOM_CONDITIONS.keys()))

# Check symptoms and display results
if st.button("Check Symptoms"):
    if selected_symptoms:
        conditions = check_symptoms(selected_symptoms)
        if conditions:
            st.success("Possible conditions based on your symptoms:")
            for condition in conditions:
                st.write(f"- {condition}")
        else:
            st.warning("No conditions found for the selected symptoms.")
    else:
        st.error("Please select at least one symptom.")

# Optional: Provide further recommendations
st.subheader("Next Steps")
st.write("If you are experiencing severe symptoms, please consult a healthcare professional.")
