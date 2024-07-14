import pandas as pd
import openmeteo_requests
import pandas as pd
from retry_requests import retry
from api_config import params

def response_as_dict(response, params: dict) -> dict:
    """Processes response for hourly data and returns the hourly parameters with its values (numpy) as dictionary.

    Args:
        response (_type_): Response of the openmeteo API call
        params (dict): Parameter dictionary that is used to perform the API call.

    Returns:
        dict: Response of hourly parameter with its values.
    """
    hourly_reponse = response.Hourly()
    hourly_params = params['hourly']
    hourly_dict = {}
    
    for param_i, param in enumerate(hourly_params):
        hourly_dict[param] = hourly_reponse.Variables(param_i).ValuesAsNumpy()
        
    return hourly_dict

def response_as_dataframe(response, params:dict) -> pd.DataFrame:
    """Processes response for hourly data and returns the hourly parameters with its values as pandas DataFrame.

    Args:
        response (_type_): Response of the openmeteo API call
        params (dict): Parameter dictionary that is used to perform the API call.

    Returns:
        pd.DataFrame: Response of hourly parameter with its values.
    """
    hourly_response = response.Hourly()
    hourly_dict = hourly_dict(response=response, params=params)
    
    hourly_dataframe = {
    'date': pd.date_range(
        start=pd.to_datetime(hourly_response.Time(), unit='s', utc=True),
        end=pd.to_datetime(hourly_response.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly_response.Interval()),
        inclusive='left'
        )
    }
    
    for param, value in hourly_dict.items():
        hourly_dataframe[param] = value
    
    return pd.DataFrame(hourly_dataframe)