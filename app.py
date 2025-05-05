import streamlit as st
import requests

#Title
st.title("Weather App")
st.write("Get the real-time weather of your city!")

#Input for city name 
city = st.text_input("Enter city name: ")

#API call
if city:
    api_key = "your_key_here"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        st.success(f"Weather in {city}:")
        st.write(f"Temperature: {temp}°C")
        st.write(f"Description: {desc}")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Wind Speed: {wind} m/s")


    else:
        st.error(f"City not found. Please enter a valid city name.")

