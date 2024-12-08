import streamlit as st
import util

# Load the saved artifacts
util.load_saved_artifacts()

# Title for the app
st.title("Bengaluru Home Price Prediction")

# Sidebar for user inputs
st.sidebar.header("User Input Parameters")

# Get location names
locations = util.get_location_names()

# Function to get user inputs
def user_input_features():
    location = st.sidebar.selectbox("Select Location", locations)
    sqft = st.sidebar.number_input("Enter Total Square Feet Area", min_value=500, step=100)
    bhk = st.sidebar.slider("Select Number of Bedrooms (BHK)", 1, 10, 2)
    bath = st.sidebar.slider("Select Number of Bathrooms", 1, 10, 2)
    return location, sqft, bhk, bath

# Get user inputs
location, sqft, bhk, bath = user_input_features()

# Prediction
if st.button("Predict Price"):
    estimated_price = util.get_estimated_price(location, sqft, bhk, bath)
    st.success(f"Estimated Home Price: ₹ {estimated_price} Lakh")

# Additional info section
st.sidebar.subheader("About the App")
st.sidebar.text("This app predicts Bengaluru home prices based on input parameters.")
