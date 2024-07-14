import requests
from .api_config import params

def get_API_response() -> dict:
    """Calling the openmetep API with parameters definde in api_config and returns the JSON dictionary response.

    Returns:
        dict: Returns the seponse data JSON dictionary of the API call
    """
    # API URL link
    url = "https://api.open-meteo.com/v1/forecast"

    # Performing API call and get response
    response = requests.get(url, params=params)

    # Getting response as dictionary
    response_data = response.json()
    
    return response_data
