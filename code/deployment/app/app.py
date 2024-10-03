# streamlit_app.py
import streamlit as st
import requests

# FastAPI endpoint
FASTAPI_URL = "http://fastapi:8000/predict"

# Streamlit app UI
st.title("Students Performance Classifier")


test_preparation_course_radio=st.radio(
    "Did you participate preparation course",
    ["Yes", "No"]
)

if test_preparation_course_radio == "Yes":
    test_preparation_course = 1
else:
    test_preparation_course = 0

math_score = st.number_input("math score", min_value=0, max_value=100)
reading_score = st.number_input("reading score", min_value=0, max_value=100)
writing_score = st.number_input("writing score", min_value=0, max_value=100)


# Make prediction when the button is clicked
if st.button("Predict"):
    # Prepare the data for the API request
    input_data = {
        "test_preparation_course": test_preparation_course,
        "math_score": math_score,
        "reading_score": reading_score,
        "writing_score": writing_score
    }

    # Send a request to the FastAPI prediction endpoint
    response = requests.post(FASTAPI_URL, json=input_data)
    prediction = response.json()["prediction"]
    if prediction == 0:
        st.success(f"You are male")
    else:
        st.success(f"You are female")

