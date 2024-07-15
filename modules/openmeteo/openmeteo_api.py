import requests
from all_imports import get_params

def get_API_response(gui_instance) -> dict:
    """Calling the openmetep API with parameters definde in api_config and returns the JSON dictionary response.

    Returns:
        dict: Returns the seponse data JSON dictionary of the API call
    """
    # API URL link
    url = "https://api.open-meteo.com/v1/forecast"

    # Performing API call and get response
    params = get_params(gui_instance)
    # print(f"Calling API with params: {params}")
    response = requests.get(url, params=params)

    # Getting response as dictionary
    response_data = response.json()
    # print(response_data)
    return response_data


if __name__ == "__main__":
    class DummyGui:
        def __init__(self):
            self.city_name = 'hamburg'

        def get_city(self):
            return self.city_name

    gui_instance = DummyGui()
    get_API_response(gui_instance)