
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.llm import gpt
from modules.weather import fetch_weater_data

daten = {
    "temperature": 30,
    "rain_percantage": 10,
    "weather_state": "cloudy",
    "wind": 20
}

data = fetch_weater_data()


prompt = f"The temperature is {data['temperature_2m_max']} degrees, the rain percentage is {data['rain_sum']}, the wind speed is {data['wind_speed_10m_max']}"
gpt(prompt)