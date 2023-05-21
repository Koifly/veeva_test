import json
import requests

def get_geocoding_info(zip_code, key):
    url = "http://api.openweathermap.org/geo/1.0/zip"
    parameters = {
    "zip" : zip_code,
    "appid" : key,
    }

    response = requests.get(url, params=parameters)
    return response


def get_weather_info(lat, lon, key):
    url = "http://api.openweathermap.org/data/2.5/forecast"
    parameters = {
    "lat" : lat,
    "lon" : lon,
    "appid" : key,
    "units" : "metric",
    }

    response = requests.get(url, params=parameters)
    return response