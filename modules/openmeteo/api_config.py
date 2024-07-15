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
        'hamburg': {
            'latitude': 53.551086,
            'longitude': 9.993682,
        },
        'muenchen': {
            'latitude': 53.551086,
            'longitude': 9.993682,
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
