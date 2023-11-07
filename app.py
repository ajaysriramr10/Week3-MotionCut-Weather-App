from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Weatherstack API key
API_KEY = 'c963f3379c0fd725f324ec357b355f51'

@app.route("/", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city_name = request.form.get("city")
        weather_data = fetch_weather_data(city_name)
        return render_template("weather.html", weather_data=weather_data)
    return render_template("index.html")

def fetch_weather_data(city_name):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": API_KEY,
        "query": city_name,
        "units": "m"  # You can adjust this to your preferred unit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        weather_data = {
            "city": data["location"]["name"],
            "temperature": data["current"]["temperature"],
            "humidity": data["current"]["humidity"],
            "description": data["current"]["weather_descriptions"][0]
        }
    except Exception as e:
        print(e)
        weather_data = None
    return weather_data

if __name__ == "__main__":
    app.run(debug=True)
