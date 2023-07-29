# save this as app.py
from flask import Flask
import requests

app = Flask('Flask')
def get_temperature_for_date(weather):
    if 'daily' in weather and 'time' in weather['daily']:
        dates = weather['daily']['time']
        if '2023-07-30' in dates:
            index = dates.index('2023-07-30')
            temp_min = weather['daily']['temperature_2m_min'][index]
            temp_max = weather['daily']['temperature_2m_max'][index]
            return f"Temperature on 2023-07-30: Min = {temp_min}°C, Max = {temp_max}°C"

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
    weather=output.json()
    # Get the wind direction from the current weather information
    wind_direction = weather['current_weather']['winddirection']
    
    # Get the temperature for the specific date using the defined function
    temperature_for_date = get_temperature_for_date(weather)

    # Return the wind direction and temperature information
    return f"Wind Direction: {wind_direction}, {temperature_for_date}"

    
