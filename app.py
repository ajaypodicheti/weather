# save this as app.py
from flask import Flask
import requests

app = Flask('Flask')

@app.route("/")
def meteo():
    meteo_Api = "https://api.open-meteo.com/v1/forecast?"
    params = {
        'latitude': '52.52',
        'longitude': '13.41',
        'daily': 'temperature_2m_min,temperature_2m_max,precipitation_sum',
        'current_weather': 'True',
        'temperature_unit': 'celsius',
        'precipitation_unit': 'mm',
        'forecast_days': '10',
        'timezone': 'Europe/London'
    }
    params['windspeed_unit'] = 'kmh'
    params['temperature_unit'] = 'celsius'
    output = requests.get(meteo_Api, params=params, verify=True)
    return output.json()
    
