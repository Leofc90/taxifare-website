import streamlit as st
import datetime
import pandas as pd
import requests

st.title("TAXI FARE PREDICTION 🚕 ")

st.header("📆Date & Time:")
# Pick the date and time :
d = st.date_input("Date:", datetime.datetime.now())
c = st.time_input("Time:", datetime.datetime.now())
#st.write("Date is:", d)
#st.write("Time is:", c)

st.header("📍Pickup and Dropoff points:")
st.subheader("Pickup Points:")
# Pickup longitude and latitude:
p_longitude = st.number_input("Pickup Longitude:")
p_latitude = st.number_input("Pickup Latitude:")
#st.write("Longitude:", p_longitude)
#st.write("Latitude:", p_latitude)

st.subheader("Dropoff Points:")
d_longitude = st.number_input("Dropoff longitude:")
d_latitude = st.number_input("Dropoff latitude:")
#st.write("Longitude:", d_longitude)
#st.write("Latitude:", d_latitude)

st.header("Number of Passenger:")
option = st.selectbox("Number of Passanger:",(1,2,3,4,5,6))
st.write("You selected:", option)

#date_time = pd.Timestamp.combine(d,c)
date_time = datetime.datetime.combine(d,c)

# Dictionary containing the parameters for our API:
params = {'pickup_datetime': [date_time],
              'pickup_longitude': [p_longitude],
              'pickup_latitude': [p_latitude],
              'dropoff_longitude': [d_longitude],
              'dropoff_latitude': [d_latitude],
              'passenger_count': [option]
}

# Calling API:
url = 'https://taxifare-588359044626.europe-west1.run.app/predict'
submitted = st.button("Submit")
if submitted:
    response = requests.get(url, params=params).json()
    if response:
        st.subheader("Response:")
        st.json(response)

# Retrieve the prediction from the JSON returned by the API:
#if response.status_code == 200:
    #result = response.json()  # Parse the JSON response
    #prediction = result.get('prediction')  # Adjust based on the response structure
#else:
    #prediction = "Error: Unable to get prediction"
