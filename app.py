from flask import Flask,render_template,request 
import requests

app = Flask('Flask')
def get_temperature_for_date(weather):
    if 'daily' in weather and 'time' in weather['daily']:
        dates = weather['daily']['time']
        if '2023-08-21' in dates:
            index = dates.index('2023-08-21')
            temp_min = weather['daily']['temperature_2m_min'][index]
            temp_max=weather['daily']
            ['temperature _2m_max'][index]
            return f"Temperature on 2023-08-21: Min = {temp_min}°C, Max = {temp_max}°C"
        else:
            return "No data available for 2023-08-21."
    else:
        return "No daily data available."
#route for the root url
@app.route("/",methods=['GET','POST'])
def meteo():
if request method=='POST':
#Get user input data
    latitude=request.form.get("latitude")
    longitude=request.form.get("longitude")
    location=request.form.get("location")
    max_temp-checkbox=
request.form.get("max_temp_checkbox")=="on"
    min_temp-checkbox=
request.form.get("min_temp_checkbox")=="on"
    precip_sum-checkbox=
request.form.get("current_weather")=="on"
    forecast_days=request.form.get("forecast_days")
    time_zone=request.form.get("time-zone")
    #Set API URL and parameters
    meteo_Api = "https://api.open-meteo.com/v1/forecast?"
    daily_params = {
    if max_temp_checkbox:
        daily_params.append("temperature_2m_max")
    if min_temp_checkbox:
        daily_params.append("temperature_2m_min")
    if precip_sum_checkbox:
        daily_params.append("precipitation_sum")
        params={
        'latitude':latitude,
        'longitude':longitude,
        'daily':",",join(daily_params),
        'current_weather':current_weather,
        'timezone':time_zone,
        'forecast_days':forecast_days
        }

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

    
