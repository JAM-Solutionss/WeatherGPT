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

# Parameters for API call
params = {
    'latitude': locations['Hamburg']['latitude'],
    'longitude': locations['Hamburg']['longitude'],
    'hourly': [
        'temperature_2m',
        'precipitation_probability', 
        'wind_speed_10m'
    ],
    'timezone': 'Europe/Berlin'
}


