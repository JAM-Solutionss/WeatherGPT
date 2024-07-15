from tkinter.messagebox import YESNOCANCEL
import plotly.express as px
import pandas as pd
import sys
import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)

from all_imports import get_API_response
from all_imports import hourly_data_dataframe
from all_imports import params


def plot(data: pd.DataFrame, xcol: str, ycol: str, fname) -> None:
    fig = px.line(
        data,
        x=xcol,
        y=ycol,
        markers=True
    )
    fig.write_image(fname)

def get_graphics(data: pd.DataFrame):
    graphics = {}   
    
    for param in params['hourly'].keys():
        
    


if __name__ == "__main__":
    class DummyGui:
        def __init__(self):
            self.city_name = 'hamburg'

        def get_city(self):
            return self.city_name

    gui_instance = DummyGui()
    resp = get_API_response(gui_instance)
    df = hourly_data_dataframe(resp)
    
    plot(df, xcol='time', ycol='temperature_2m')

    