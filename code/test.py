import sys, os

# Fügen Sie den relativen Pfad zu dem Verzeichnis 'code' und 'all_imports' hinzu
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)

from all_imports import hallo

print(hallo)