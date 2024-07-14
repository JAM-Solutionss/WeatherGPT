import re
import pandas as pd
import openmeteo_requests
import pandas as pd
from retry_requests import retry
from api_config import params

def response_as_dict(response, params: dict) -> dict:
    """Processes response data and returns the parameters with its values as dictionary.

    Args:
        response (_type_): Response of the openmeteo API call
        params (dict): Parameter dictionary that is used to perform the API call.

    Returns:
        dict: Response parameters with its values.
    """
    response_data = {}
    response_data['current'] = response.Current()
    response_data['hourly'] = response.Hourly()
    response_data['daily'] = response.Daily()

    response_dict = {}
    
    for forecast, data in response_data.items():
        
        response_dict[forecast] = {}
             
        for param_i, param in enumerate(params[forecast]):
            response_dict[forecast][param] = response_data[forecast].Variables(param_i).ValuesAsNumpy()
        
    return response_dict

# def response_as_dataframe(response, params:dict) -> pd.DataFrame:
#     """Processes response data and returns the parameters with its values as pandas DataFrame.

#     Args:
#         response (_type_): Response of the openmeteo API call
#         params (dict): Parameter dictionary that is used to perform the API call.

#     Returns:
#         pd.DataFrame: Response parameters with its values.
#     """
#     response_data = response.Hourly()
#     hourly_dict = hourly_dict(response=response, params=params)
    
#     hourly_dataframe = {
#     'date': pd.date_range(
#         start=pd.to_datetime(response_data.Time(), unit='s', utc=True),
#         end=pd.to_datetime(response_data.TimeEnd(), unit="s", utc=True),
#         freq=pd.Timedelta(seconds=response_data.Interval()),
#         inclusive='left'
#         )
#     }
    
#     for param, value in hourly_dict.items():
#         hourly_dataframe[param] = value
    
#     return pd.DataFrame(hourly_dataframe)