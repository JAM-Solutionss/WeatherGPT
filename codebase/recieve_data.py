
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from modules.llm import gpt
#from modules.weather import fetch_weater_data
#from modules.openmeteo import get_API_response, hourly_data_dict
from all_imports import gpt, get_API_response, hourly_data_dict


def get_llm_response(gui_instance):
    
    response = get_API_response(gui_instance)
    hourly_data_dictionary = hourly_data_dict(response)
    data = hourly_data_dictionary
    #print(data)

    prompt = f"Todays Weather: The temperature is {data['temperature_2m']} degrees, the rain probability is {data['precipitation_probability']}, the wind speed is {data['wind_speed_10m']}"
    return gpt(prompt)

if __name__ == "__main__":
    class DummyGui:
        def __init__(self):
            self.city_name = 'hamburg'

        def get_city(self):
            return self.city_name

    gui_instance = DummyGui()
    get_llm_response(gui_instance)
