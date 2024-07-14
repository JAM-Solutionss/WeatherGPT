import requests
from api_config import params
from data_processor import hourly_data_dict

# API URL link
url = "https://api.open-meteo.com/v1/forecast"

# Performing API call and get response
response = requests.get(url, params=params)
response_data = response.json()
hourly_data = hourly_data_dict(response_data)
