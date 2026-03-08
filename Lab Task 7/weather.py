"""
Wrapper module for Ambee geocoding and weather endpoints.

This module expects the `API_WEATHER` key to be available in the environment,
typically loaded from a `.env` file.
"""

import requests
import os 
from dotenv import load_dotenv

load_dotenv()

class WeatherClient:
    """Simple client for Ambee geocode and weather API endpoints.

    The client requires a valid Ambee API key and returns parsed JSON payloads
    from each endpoint.
    """

    def __init__(self,api):
        """Initialize the Weather client.

        Args:
            api: Ambee API key used in request headers.
        """
        self.api_key = api

    def geo(self , city):
        """Fetch geocoding data for a city/place name.

        Args:
            city: Name of the city or place to geocode.

        Returns:
            Parsed JSON response from the geocoding endpoint.
        """

        headers = {
            'x-api-key': self.api_key,
            'Content-type': "application/json"
        }

        geourl = f"https://api.ambeedata.com/geocode/by-place?place={city}"

        geo_responce = requests.get(url=geourl, headers=headers)
       
        return  geo_responce.json()

    def weather_now(self,lon,lat):
        """Fetch the latest weather data by coordinates.

        Args:
            lon: Longitude value.
            lat: Latitude value.

        Returns:
            Parsed JSON response from the latest weather endpoint.
        """

        headers = {
            'x-api-key': self.api_key,
            'Content-type': "application/json"
        }

        weather_url = f"https://api.ambeedata.com/weather/latest/by-lat-lng?lat={lat}&lng={lon}"

        weather_responce = requests.get(weather_url,headers)
        return weather_responce.json()
    
    def weather_history(self,longitute,latitute ,fr,to):
        """Fetch historical weather data for a coordinate range and time window.

        Args:
            longitute: Longitude value.
            latitute: Latitude value.
            fr: Start date/time for history query (i.e YYYY-MM-DD hh:mm:ss).
            to: End date/time for history query (i.e YYYY-MM-DD hh:mm:ss).

        Returns:
            Parsed JSON response from the historical weather endpoint.
        """
        headers = {
            'x-api-key': self.api_key,
            'Content-type': "application/json"
        }

        weather_url = f"https://api.ambeedata.com/weather/history/by-lat-lng?lat={latitute}&lng={longitute}&from={fr}&to={to}"

        weather_responce = requests.get(weather_url,headers)
        return weather_responce.json()

if __name__ == '__main__':
    city = "Lahore"
    API = os.getenv('API_WEATHER')
    obj = WeatherClient(API)
    a = obj.geo(city)
    print(a)
    print("------------------------------------")
    latitute = a['data'][0]['lat']
    longitute = a['data'][0]['lng']
    # print(obj.weather_now(longitute,latitute))
    print("-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(obj.weather_history(longitute,latitute,'2026-03-05 00:00:00','2026-03-06 00:00:00'))
