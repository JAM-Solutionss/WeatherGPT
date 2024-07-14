import requests
from api_config import params

# API URL link
url = "https://api.open-meteo.com/v1/forecast"

# Performing API call and get response
response = requests.get(url, params=params)
response_data = response.json()
