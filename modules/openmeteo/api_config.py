import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from code.gui import Gui
# Configurations for API Call
# Some predefined locations
locations = {
    'hamburg': {
        'latitude': 53.551086,
        'longitude': 9.993682,
    },
    'muenchen': {
        'latitude': 53.551086,
        'longitude': 9.993682,
    }
}

city = Gui().city()
print(city)


# Parameters for API call
params = {
    "forecast_days": 1,
    'latitude': locations[f'{city}']['latitude'],
    'longitude': locations[f'{city}']['longitude'],
    'hourly': [
        'temperature_2m',
        'precipitation_probability', 
        'wind_speed_10m'
    ],
    'timezone': 'Europe/Berlin'
}


