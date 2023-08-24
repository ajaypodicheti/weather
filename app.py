# Import necessary modules
from flask import Flask, render_template, request
import requests

# Create a Flask application instance
app = Flask(__name__)

# Function to get temperature information for a specific date
def get_temperature_for_date(weather):
    if 'daily' in weather and 'time' in weather['daily']:
        dates = weather['daily']['time']
        if '2023-08-21' in dates:
            index = dates.index('2023-08-21')
            temp_min = weather['daily']['temperature_2m_min'][index]
            temp_max = weather['daily']['temperature_2m_max'][index]
            return f"Temperature on 2023-08-21: Min = {temp_min}°C, Max = {temp_max}°C"
        else:
            return "No data available for 2023-08-21."
    else:
        return "No daily data available."

# Route for the root URL
@app.route("/", methods=['GET', 'POST'])
def meteo():
    if request.method == 'POST':
        # Get user input data
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        location = request.form.get("location")
        max_temp_checkbox = request.form.get("max_temp_checkbox") == "on"
        min_temp_checkbox = request.form.get("min_temp_checkbox") == "on"
        precip_sum_checkbox = request.form.get("precip_sum_checkbox") == "on"
        current_weather = request.form.get("current_weather") == "on"
        temperature_unit = request.form.get("temperature_unit")
        wind_speed_unit = request.form.get("wind_speed_unit")
        forecast_days = request.form.get("forecast_days")
        time_zone = request.form.get("time_zone")

        # Set API URL and parameters
        meteo_api = "https://api.open-meteo.com/v1/forecast"
        daily_params = []
        if max_temp_checkbox:
            daily_params.append("temperature_2m_max")
        if min_temp_checkbox:
            daily_params.append("temperature_2m_min")
        if precip_sum_checkbox:
            daily_params.append("precipitation_sum")

        params = {
            'latitude': latitude,
            'longitude': longitude,
            'daily': ",".join(daily_params),
            'current_weather': current_weather,
            'temperature_unit': temperature_unit,
            'wind_speed_unit': wind_speed_unit,
            'timezone': time_zone,
            'forecast_days': forecast_days
        }

        # Make API request and retrieve weather data
        output = requests.get(meteo_api, params=params, verify=True)
        weather = output.json()

        # Get wind direction and temperature for a specific date
        wind_direction = weather.get('current_weather', {}).get('winddirection', 'N/A')
        temperature_for_date = get_temperature_for_date(weather)

        # Render the template with retrieved data
        return render_template('index.html', wind_direction=wind_direction, temperature_for_date=temperature_for_date)

    # Render the template initially
    return render_template('index.html')

# Run the application if executed as the main script
if __name__ == "_main_":
    app.run(debug=True)