from flask import Flask, request, render_template
from weather import WeatherClient
from dotenv import load_dotenv
import os 

load_dotenv()

api = os.getenv("API_WEATHER")

weather = WeatherClient(api)

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/")
def home():
    data = {
        'message': "Weather API Server",
        'routes': [
            '/info/<city>',
            '/weather?lng=0000.00&lat=0000.00',
            '/current/<city>',
            '/history/<city>?from=YYYY-MM-DD hh:mm:ss&to=YYYY-MM-DD hh:mm:ss'
        ]
    }
    return render_template('home.html', data=data)


@app.route("/info/<city>")
def info(city):
    geo = weather.geo(city)

    if geo['message'] != 'success':
        data = {
            'error': 'Api Error',
            'details': geo
        }
        return render_template('error.html', data=data), 500
    
    if not geo['data']:
        data = {
            'error': 'City Not Found',
            'city': city
        }
        return render_template('error.html', data=data), 404

    location = geo['data'][0]
    lat = location['lat']
    lng = location['lng']

    address = location['address']
    city_name = address['city']
    country = address['countryName']
    code = address['countryCode']

    data = {
        "message": "success",
        "city": city_name,
        "country": country,
        "country_code": code,
        "latitude": lat,
        "longitude": lng
    }
    
    return render_template('info.html', data=data)


@app.route("/weather")
def weather_by_coordinates():
    longitude = request.args.get("lng")
    latitude = request.args.get("lat")

    if not longitude or not latitude:
        data = {"error": "longitude and latitude required"}
        return render_template('error.html', data=data), 400

    res = weather.weather_now(longitude, latitude)
    weather_data = res['data']

    data = {
        "message": "success",
        "latitude": weather_data["lat"],
        "longitude": weather_data["lng"],
        "country_code": weather_data["country_code"],
        "timezone": weather_data["timezone"],
        "temperature": weather_data["temperature"],
        "feels_like": weather_data["apparentTemperature"],
        "summary": weather_data["summary"],
        "icon": weather_data["icon"],
        "humidity": weather_data["humidity"],
        "dew_point": weather_data["dewPoint"],
        "pressure": weather_data["pressure"],
        "surface_pressure": weather_data["surfacePressure"],
        "visibility": weather_data["visibility"],
        "ozone": weather_data["ozone"],
        "wind_speed": weather_data["windSpeed"],
        "wind_gust": weather_data["windGust"],
        "wind_direction": weather_data["windBearing"],
        "precip_probability": weather_data["precipProbability"],
        "precip_intensity": weather_data["precipIntensity"],
        "uv_index": weather_data["uvIndex"],
        "updated_at": weather_data["updatedAt"]
    }
    
    return render_template('current.html', data=data)


@app.route("/current/<city>")
def current_weather(city):
    geo = weather.geo(city)

    if geo['message'] != 'success':
        data = {
            'error': 'Api Error',
            'details': geo
        }
        return render_template('error.html', data=data), 500
    
    if not geo['data']:
        data = {
            'error': 'City Not Found',
            'city': city
        }
        return render_template('error.html', data=data), 404

    lat = geo["data"][0]["lat"]
    lon = geo["data"][0]["lng"]
    city_name = geo["data"][0]["address"]["city"]

    current = weather.weather_now(lon, lat)
    weather_data = current['data']

    data = {
        'message': 'success',
        'city': city_name,
        'latitude': weather_data['lat'],
        'longitude': weather_data['lng'],
        'country_code': weather_data['country_code'],
        'timezone': weather_data['timezone'],
        'temperature': weather_data["temperature"],
        'feels_like': weather_data["apparentTemperature"],
        'summary': weather_data["summary"],
        'icon': weather_data["icon"],
        'humidity': weather_data["humidity"],
        'dew_point': weather_data["dewPoint"],
        'pressure': weather_data["pressure"],
        'surface_pressure': weather_data["surfacePressure"],
        'visibility': weather_data["visibility"],
        'ozone': weather_data["ozone"],
        'wind_speed': weather_data["windSpeed"],
        'wind_gust': weather_data["windGust"],
        'wind_direction': weather_data["windBearing"],
        'precip_probability': weather_data["precipProbability"],
        'precip_intensity': weather_data["precipIntensity"],
        'uv_index': weather_data["uvIndex"],
        'updated_at': weather_data["updatedAt"].replace("T", " ").replace("Z", "")
    }
    
    return render_template('current.html', data=data)


@app.route("/history/<city>")
def weather_history(city):
    fr = request.args.get("from")
    to = request.args.get("to")

    if not fr or not to:
        data = {"error": "from and to parameters required"}
        return render_template('error.html', data=data), 400

    geo = weather.geo(city)

    if geo['message'] != 'success':
        data = {
            'error': 'Api Error',
            'details': geo
        }
        return render_template('error.html', data=data), 500
    
    if not geo['data']:
        data = {
            'error': 'City Not Found',
            'city': city
        }
        return render_template('error.html', data=data), 404

    lat = geo["data"][0]["lat"]
    lon = geo["data"][0]["lng"]
    city_name = geo["data"][0]["address"]["city"]

    response = weather.weather_history(lon, lat, fr, to)
    if not response['data']:
        data = {
            'error': "Error",
            'details': response['message']
        }
        return render_template('error.html', data=data), 400
    
    history = response['data']['history']
    formatted = []
    
    for i in history:
        formatted.append({
            'time': i['createdAt'].replace("T", " ").replace("Z", ""),
            'temperature': i["temperature"],
            'feels_like': i["apparentTemperature"],
            'summary': i["summary"],
            'icon': i["icon"],
            'humidity': i["humidity"],
            'dew_point': i["dewPoint"],
            'pressure': i["pressure"],
            'visibility': i["visibility"],
            'wind_speed': i["windSpeed"],
            'wind_gust': i["windGust"],
            'wind_direction': i["windBearing"],
            'precip_probability': i["precipProbability"],
            'precip_intensity': i["precipIntensity"],
            'uv_index': i["uvIndex"],
            'cloud_cover': i["cloudCover"]
        })

    data = {
        'message': 'success',
        'city': city_name,
        'longitude': lon,
        'latitude': lat,
        'from': fr,
        'to': to,
        'history': formatted
    }
    
    return render_template('history.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
