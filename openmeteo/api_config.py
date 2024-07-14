# Configurations for API Call

# Defining variables to be requested
variables = [
    'temperature_2m',
    "relative_humidity_2m", 
    "apparent_temperature", 
    "precipitation_probability", 
    "rain", "surface_pressure", 
    "cloud_cover", 
    "wind_speed_10m", 
    "uv_index"
]

# Parameters for API call
params = {
    'latitude': 52.52,
    'longitude': 13.41,
    'current': variables,
    'hourly': variables,
    'daily': variables,    
    'timezone': 'Europe/Berlin'
}

# Location - Placeholder for later
location = {}