from flask import Flask,request
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
    return (
        {
            'message' : "Server is Runnning",
            'routes' : [
                '/info/<city>',
                '/weather?lng=0000.00&lat=0000.00',
                '/weather/current/<city>',
                '/weather/history/<city>?from=YYYY-MM-DD hh:mm:ss&toYYYY-MM-DD hh:mm:ss'
                ]
        }
    )



@app.route("/info/<city>")
def info(city):

    geo = weather.geo(city)

    if geo['message'] != 'success':
        return ({
            'message' : 'Api Error',
            'details' : geo
        }) , 500
    
    if not geo['data'] :
        return ({
            'message' : 'City Not Found'
        }) , 404


    data = geo['data'][0]
    lat = data['lat']
    lng = data['lng']

    address = data['address']
    city_name = address['city']
    country = address['countryName']
    code = address['countryCode']

    return ({
        "message": "success",
        "location": {
            "city": city_name,
            "country": country,
            "country_code": code,
        },
        "coordinates": {
            "latitude": lat,
            "longitude": lng
        }
    })



@app.route("/weather")
def weather_by_coordinates():

    longitude = request.args.get("lng")
    latitude = request.args.get("lat")

    if not longitude or not latitude:
        return ({"error": "longitude and latitude required"}), 400

    res = weather.weather_now(longitude, latitude)
    data = res['data']


    return ({
        "message": "success",

        "location": {
            "latitude": data["lat"],
            "longitude": data["lng"],
            "country_code": data["country_code"],
            "timezone": data["timezone"]
        },

        "weather": {
            "temperature": data["temperature"],
            "feels_like": data["apparentTemperature"],
            "summary": data["summary"],
            "condition": data["icon"]
        },

        "atmosphere": {
            "humidity": data["humidity"],
            "dew_point": data["dewPoint"],
            "pressure": data["pressure"],
            "surface_pressure": data["surfacePressure"],
            "visibility": data["visibility"],
            "ozone": data["ozone"]
        },

        "wind": {
            "speed": data["windSpeed"],
            "gust": data["windGust"],
            "direction": data["windBearing"]
        },

        "precipitation": {
            "probability": data["precipProbability"],
            "intensity": data["precipIntensity"]
        },

        "uv_index": data["uvIndex"],
        "updated_at": data["updatedAt"]
    })



@app.route("/weather/current/<city>")
def current_weather(city):

    geo = weather.geo(city)

    lat = geo["data"][0]["lat"]
    lon = geo["data"][0]["lng"]

    current = weather.weather_now(lon, lat)
    data = current['data']

    return ({
        'message': 'success',

        'location':{
            'latitude': data['lat'],
            'longitude' : data['lng'],
            'country_code' : data['country_code'],
            'time_zone' : data['timezone']
        },

        'weather':{
            "temperature": data["temperature"],
            "feels_like": data["apparentTemperature"],
            "summary": data["summary"],
            "icon": data["icon"]
        },

        "atmosphere": {
            "humidity": data["humidity"],
            "dew_point": data["dewPoint"],
            "pressure": data["pressure"],
            "surface_pressure": data["surfacePressure"],
            "visibility": data["visibility"],
            "ozone": data["ozone"]
        },

        "wind": {
            "speed": data["windSpeed"],
            "gust": data["windGust"],
            "direction": data["windBearing"]
        },

        "precipitation": {
            "probability": data["precipProbability"],
            "intensity": data["precipIntensity"]
        },

        "uv_index": data["uvIndex"],
        "updated_at": data["updatedAt"].replace("T"," ").replace("Z","")
    })


# Weather history
@app.route("/weather/history/<city>")
def weather_history(city):

    fr = request.args.get("from")
    to = request.args.get("to")

    if not fr or not to:
        return ({"error": "from and to parameters required"}), 400

    geo = weather.geo(city)

    lat = geo["data"][0]["lat"]
    lon = geo["data"][0]["lng"]

    responce = weather.weather_history(lon, lat, fr, to)
    if not responce['data'] :
        return ({
            'message' : "Error",
            'Detail' : responce['message']
        }),400
    
    history = responce['data']['history']
    formated = []
    
    for i in history:
        formated.append({
            'time' : i['createdAt'].replace("T"," ").replace("Z",""),
            'weather':{
                "temperature": i["temperature"],
                "feels_like": i["apparentTemperature"],
                "summary": i["summary"],
                "icon": i["icon"]
            },

            "atmosphere": {
                "humidity": i["humidity"],
                "dew_point": i["dewPoint"],
                "pressure": i["pressure"],
                "visibility": i["visibility"],
            },

            "wind": {
                "speed": i["windSpeed"],
                "gust": i["windGust"],
                "direction": i["windBearing"]
            },

            "precipitation": {
                "probability": i["precipProbability"],
                "intensity": i["precipIntensity"]
            },

            "uv_index": i["uvIndex"],
            "cloud_cover": i["cloudCover"]

        })


    return ({
        'message' : 'success',
        'location': {
            'longitude': lon,
            'latitude': lat,
        },

        'history' : formated 
    })



if __name__ == "__main__":
    app.run(debug=True)
