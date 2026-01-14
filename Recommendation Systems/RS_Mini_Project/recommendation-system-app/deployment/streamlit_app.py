import streamlit as st
import pandas as pd
from src.data.load_data import load_data
from src.models.predict import make_predictions

# Load the processed data
data = load_data('data/processed/processed_data.csv')

# Title of the app
st.title("Recommendation System")

# Sidebar for user input
st.sidebar.header("User Input")

# Example user input fields (customize as needed)
user_input = st.sidebar.text_input("Enter your preferences:")

# Button to get recommendations
if st.sidebar.button("Get Recommendations"):
    recommendations = make_predictions(user_input, data)
    st.subheader("Recommendations")
    st.write(recommendations)

# Display the dataset
st.subheader("Dataset Overview")
st.write(data.head())