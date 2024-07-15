
import sys
import os

# from code.gui import Gui
# from code.recieve_data import get_llm_response
from modules.openmeteo import get_API_response, hourly_data_dict

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from modules.speech import create_audio

hallo = 1234