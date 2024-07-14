import re
from urllib import response
import pandas as pd
import openmeteo_requests
import pandas as pd
from retry_requests import retry
from api_config import params

def current_data_dict(response_json: dict) -> dict:
    if 'current' in response_json.keys():
        return response_json['current']
    else: 
        return None
    
def hourly_data_dict(response_json: dict) -> dict:
    if 'hourly' in response_json.keys():
        return response_json['hourly']
    else: 
        return None
    
def daily_data_dict(response_json: dict) -> dict:
    if 'daily' in response_json.keys():
        return response_json['daily']
    else: 
        return None




def data_as_dict(forecast_data) -> dict[dict]:
    """Processes response data and returns the parameters with its values as dictionary.

    Args:
        response (_type_): Response of the openmeteo API call
        params (dict): Parameter dictionary that is used to perform the API call.

    Returns:
        dict[dict]: Response parameters with its values for 'current', 'hourly' and 'daily' forecast.
    """
       
    return forecast_data

def response_as_dataframe(response, params:dict) -> dict[pd.DataFrame]:
    """Processes response data and returns the parameters with its values as pandas DataFrame.

    Args:
        response (_type_): Response of the openmeteo API call
        params (dict): Parameter dictionary that is used to perform the API call.

    Returns:
        dict[pd.DataFrame]: Response parameters with its values for 'current', 'hourly' and 'daily' forecast in pandas DataFrame format
    """
    response_data = response.Hourly()
    hourly_dict = hourly_dict(response=response, params=params)
    
    hourly_dataframe = {
    'date': pd.date_range(
        start=pd.to_datetime(response_data.Time(), unit='s', utc=True),
        end=pd.to_datetime(response_data.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=response_data.Interval()),
        inclusive='left'
        )
    }
    
    for param, value in hourly_dict.items():
        hourly_dataframe[param] = value
    
    return pd.DataFrame(hourly_dataframe)