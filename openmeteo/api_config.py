# Configurations for API Call

# Defining variables to be requested
variables = [

]

# Parameters for API call
params = {
    'latitude': 52.52,
    'longitude': 13.41,
    'current': [
        'temperature_2m', 
        'relative_humidity_2m', 
        'apparent_temperature', 
        'rain'
        ],
    'hourly': [
        'temperature_2m',
        'relative_humidity_2m', 
        'apparent_temperature', 
        'precipitation_probability', 
        'rain', 'surface_pressure', 
        'cloud_cover', 
        'wind_speed_10m', 
        'uv_index'
    ],
    'daily': [
        'temperature_2m_max', 
        'temperature_2m_min', 
        'apparent_temperature_max', 
        'apparent_temperature_min', 
        'uv_index_max', 
        'rain_sum'
        ],    
    'timezone': 'Europe/Berlin'
}

# Location - Placeholder for later
location = {}