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
         'timezone': 'Europe/London'
    }
    output = requests.get(meteo_Api, params=params, verify=False)
    return output.json()
    
