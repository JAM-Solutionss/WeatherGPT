import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from all_imports import Gui
#from codebase.gui import Gui
def get_city_name(gui_instance):
    city_name = gui_instance.get_city()
    # print(f"City name from gui_instance: {city_name}")
    return city_name
 


def get_params(gui_instance):
    # Configurations for API Call
    # Some predefined locations
    locations = {
        "hamburg": {
            "latitude": 53.5507,
            "longitude": 9.9930
        },
        "muenchen": {
            "latitude": 48.1374,
            "longitude": 11.5755
        },
        "berlin": {
            "latitude": 52.5244,
            "longitude": 13.4105
        },
        "koeln": {
            "latitude": 50.9333,
            "longitude": 6.9500
        },
        "frankfurt": {
            "latitude": 50.1155,
            "longitude": 8.6842
        },
        "essen": {
            "latitude": 51.4566,
            "longitude": 7.0123
        },
        "leipzig": {
            "latitude": 51.3396,
            "longitude": 12.3713
        },
        "dortmund": {
            "latitude": 51.5149,
            "longitude": 7.4660
        },
        "stuttgart": {
            "latitude": 48.7823,
            "longitude": 9.1770
        },
        "duesseldorf": {
            "latitude": 51.2217,
            "longitude": 6.7762
        }
    }
    # Parameters for API call
    city = get_city_name(gui_instance)
    # print(f"Using city: {city} for API parameters")
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
    return params

if __name__ == "__main__":
    class DummyGui:
        def __init__(self):
            self.city_name = 'hamburg'

        def get_city(self):
            return self.city_name

    gui_instance = DummyGui()
    # print(get_params(gui_instance))
