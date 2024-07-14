import requests
from api_config import params
from data_processor import hourly_data_dict, hourly_data_dataframe
import plotly.express as px

# API URL link
url = "https://api.open-meteo.com/v1/forecast"

# Performing API call and get response
response = requests.get(url, params=params)

# Getting response as dictionary
response_data = response.json()

# Extracting forecast data, e.g. hourly
hourly_data_dicctionary = hourly_data_dict(response_data)
hourly_data_df = hourly_data_dataframe(response_data)


