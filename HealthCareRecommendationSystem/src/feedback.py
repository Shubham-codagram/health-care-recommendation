import streamlit as st
import pandas as pd

# Initialize session state for feedback
if 'feedback_list' not in st.session_state:
    st.session_state.feedback_list = []

# Title
st.title("User Feedback")

# User Input Form
with st.form(key='feedback_form'):
    user_name = st.text_input("Your Name (optional)")
    feedback_text = st.text_area("Your Feedback", height=150)

    # Submit button
    submit_button = st.form_submit_button(label='Submit Feedback')

    if submit_button:
        if feedback_text:
            feedback_entry = {
                "Name": user_name if user_name else "Anonymous",
                "Feedback": feedback_text
            }
            # Append new feedback to session state list
        
