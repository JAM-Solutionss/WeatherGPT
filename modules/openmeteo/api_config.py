# Configurations for API Call

# Some predefined locations
locations = {
    'Hamburg': {
        'latitude': 53.551086,
        'longitude': 9.993682,
    },
    'München': {
        'latitude': 53.551086,
        'longitude': 9.993682,
    }
}

city = 'München'

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


