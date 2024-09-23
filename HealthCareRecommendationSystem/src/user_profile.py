import streamlit as st
import pandas as pd

# Initialize session state to store user profiles
if 'user_profiles' not in st.session_state:
    st.session_state.user_profiles = pd.DataFrame(columns=["Name", "Age", "Gender", "Location", "Health History", "Lifestyle Factors"])

# Title
st.title("User Profile Creation")

# User Input Form
with st.form(key='user_profile_form'):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
    location = st.text_input("Location")
    health_history = st.text_area("Health History (e.g., allergies, conditions)")
    lifestyle_factors = st.text_area("Lifestyle Factors (e.g., diet, exercise habits)")

    # Submit button
    submit_button = st.form_submit_button(label='Create Profile')

    if submit_button:
        new_profile = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Location": location,
            "Health History": health_history,
            "Lifestyle Factors": lifestyle_factors
        }
        # Append new profile to session state DataFrame
        st.session_state.user_profiles = st.session_state.user_profiles.append(new_profile, ignore_index=True)
        st.success("Profile created successfully!")

# Display the user profiles
if not st.session_state.user_profiles.empty:
    st.subheader("User Profiles")
    st.write(st.session_state.user_profiles)
