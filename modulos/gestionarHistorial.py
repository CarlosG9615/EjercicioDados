import json
from datetime import datetime

def guardar_historial(entry, path="historial.json"):
    try:
        with open(path, "r") as f:
            historial = json.load(f)
    except FileNotFoundError:
        historial = []
    historial.append(entry)
    with open(path, "w") as f:
        json.dump(historial, f, indent=2)

def cargar_historial(path="historial.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []