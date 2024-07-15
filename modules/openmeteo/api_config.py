import sys
import os

# Fügen Sie den relativen Pfad zu dem Verzeichnis 'code' hinzu
code_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'code'))
sys.path.append(code_path)

# Debug-Ausgabe um sicherzustellen, dass der Pfad korrekt hinzugefügt wurde
print(f"Code-Verzeichnis zu sys.path hinzugefügt: {code_path}")
print(f"Aktuelles sys.path: {sys.path}")

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

def get_city():
    # Importieren Sie das Modul innerhalb der Funktion
    from code.gui import Gui
    city_instance = Gui()
    return city_instance.city()

selected_city = get_city()
print(selected_city)



# Parameters for API call
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


