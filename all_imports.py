
import sys
import os

#from codebase import *

from modules.llm import gpt
from modules.speech import create_audio
from modules.openmeteo.data_processor import hourly_data_dict
from modules.openmeteo.data_processor import hourly_data_dataframe
from modules.openmeteo.api_config import params
from modules.openmeteo.api_config import get_params
from modules.openmeteo.openmeteo_api import get_API_response
from codebase.recieve_data import get_llm_response





