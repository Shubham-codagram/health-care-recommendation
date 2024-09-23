import streamlit as st

# Title
st.title("Mental Health Assessment")

# Introduction
st.write("Please answer the following questions to assess your mental health.")

# User Input: Questions
question_1 = st.selectbox("How often have you felt nervous, anxious, or on edge?", 
                           ["Select", "Not at all", "Several days", "More than half the days", "Nearly every day"])

question_2 = st.selectbox("How often have you felt down, depressed, or hopeless?", 
                           ["Select", "Not at all", "Several days", "More than half the days", "Nearly every day"])

question_3 = st.selectbox("How often have you had little interest or pleasure in doing things?", 
                           ["Select", "Not at all", "Several days", "More than half the days", "Nearly every day"])

question_4 = st.selectbox("How often have you felt fatigued or low on energy?", 
                           ["Select", "Not at all", "Several days", "More than half the days", "Nearly every day"])

# Submit button
if st.button("Submit Assessment"):
    responses = [question_1, question_2, question_3, question_4]
    
    if "Select" in responses:
        st.error("Please answer all questions.")
    else:
        score = sum([1 if response == "Several days" else 2 if response == "More than half the days" else 3 if response == "Nearly every day" else 0 for response in responses])
        
        st.success("Your assessment is complete!")
        
        # Provide insights based on score
        if score <= 3:
            st.write("Your responses suggest that you are doing well. However, always prioritize your mental health.")
        elif 4 <= score <= 7:
            st.write("You may be experiencing some symptoms of stress or anxiety. Consider talking to a friend or a mental health professional.")
        else:
            st.write("It appears you are facing significant challenges. We strongly recommend reaching out to a mental health professional for support.")

# Further Recommendations
st.subheader("Resources")
st.write("If you are in crisis or need immediate support, please contact a local mental health service or hotline.")
