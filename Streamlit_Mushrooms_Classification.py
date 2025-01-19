import streamlit as st
import requests
import json

# Define the endpoint URL
url = 'https://cloud-project-vjwag.eastus.inference.ml.azure.com/score'

# Function to make a POST request to the endpoint
def send_request(input_data, api_key):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    try:
        response = requests.post(url, headers=headers, json=input_data)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit App
st.title("Azure ML Endpoint Request - Mushroom Classification")

# Input fields for user
api_key = st.text_input("Enter your API key", type="password")  # Keep it secure
input_data_text = st.text_area("Enter JSON input data", height=200)

if st.button("Send Request"):
    if api_key and input_data_text:
        try:
            input_data = json.loads(input_data_text)
            response_data = send_request(input_data, api_key)
            st.success("Response received successfully!")
            st.json(response_data)
        except json.JSONDecodeError:
            st.error("Invalid JSON input")
    else:
        st.error("Please provide both API key and input data")
