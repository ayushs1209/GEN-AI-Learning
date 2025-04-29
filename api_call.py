from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather_data(city_name):
    url = f"https://wttr.in/{city_name}?format=3"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city_name} is {response.text}"
    return "Something Went Wrong"

city = input("Enter the name of the city \n")
print(get_weather_data(city))