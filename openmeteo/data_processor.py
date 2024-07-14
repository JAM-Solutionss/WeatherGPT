
import pandas as pd

def current_data_dict(response_json: dict) -> dict:
    """Extracts current forecast data from response dictionary in separate dictionary.

    Args:
        response_json (dict): Dictionary of JSON response from API call

    Returns:
        dict: Dictionary of current forecast data.
    """
    if 'current' in response_json.keys():
        return response_json['current']
    else: 
        return None
    
def hourly_data_dict(response_json: dict) -> dict:
    """Extracts hourly forecast data from response dictionary in separate dictionary.

    Args:
        response_json (dict): Dictionary of JSON response from API call

    Returns:
        dict: Dictionary of hourly forecast data.
    """
    if 'hourly' in response_json.keys():
        return response_json['hourly']
    else: 
        return None
    
def daily_data_dict(response_json: dict) -> dict:
    """Extracts daily forecast data from response dictionary in separate dictionary.

    Args:
        response_json (dict): Dictionary of JSON response from API call

    Returns:
        dict: Dictionary of daily forecast data.
    """
    if 'daily' in response_json.keys():
        return response_json['daily']
    else: 
        return None

def current_data_dataframe(response_json: dict) -> pd.DataFrame:
    """Extracts current forecast data from response dictionary in separate dataframe.

    Args:
        response_json (dict): Dictionary of JSON response from API call

    Returns:
        pd.DataFrame: Dataframe of current forecast data.
    """
    if 'current' in response_json.keys():
        return pd.DataFrame(response_json['current'])
    else: 
        return None
        
def hourly_data_dataframe(response_json: dict) -> pd.DataFrame:
    """Extracts hourly forecast data from response dictionary in separate dataframe.

    Args:
        response_json (dict): Dictionary of JSON response from API call

    Returns:
        pd.DataFrame: Dataframe of hourly forecast data.
    """
    if 'hourly' in response_json.keys():
        return pd.DataFrame(response_json['hourly'])
    else: 
        return None
    
def daily_data_dataframe(response_json: dict) -> pd.DataFrame:
    """Extracts daily forecast data from response dictionary in separate dataframe.

    Args:
        response_json (dict): Dictionary of JSON response from API call

    Returns:
        pd.DataFrame: Dataframe of daily forecast data.
    """
    if 'daily' in response_json.keys():
        return pd.DataFrame(response_json['daily'])
    else: 
        return None
