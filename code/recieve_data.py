
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.llm import gpt
from modules.weather import fetch_weater_data
from modules.openmeteo.openmeteo_api import get_data


daten = {
    "temperature": 30,
    "rain_percantage": 10,
    "weather_state": "cloudy",
    "wind": 20
}

data = get_data()


prompt = f"The temperature is {data['temperature_2m']} degrees, the rain probability is {data['precipitation_probability']}, the wind speed is {data['wind_speed_10m']}"
gpt(prompt)