#!/usr/bin/env python3
import requests
import argparse
from . data_processing import get_lat_lon, parse_weather_data
from . api_calls import get_geocoding_info, get_weather_info

argParser = argparse.ArgumentParser()
argParser.add_argument("-z", "--zip", help="Any US zip code")
argParser.add_argument("-k", "--apikey", help="Your personal API key")

def display_data(weather):
    print("# Date Temperature Precipitation")

    for day in weather:
        day_weather = "# {} {}/{} {}"
        print(day_weather.format(
            day["date"], day["hi"], day["lo"], round(day["rain"], 2)
        ))


if __name__ == "__main__":
    args = argParser.parse_args()
    zip_code = args.zip
    key = args.apikey
    try:
        geo_response = get_geocoding_info(zip_code, key)
        geo_response.raise_for_status()
        try:
            lat, lon = get_lat_lon(geo_response.json())
            weather_response = get_weather_info(lat, lon, key)
            weather_response.raise_for_status()

            parsed_data = parse_weather_data(weather_response.json())
            display_data(parsed_data)
        except requests.exceptions.HTTPError as error:
            print(error)
        except requests.ConnectionError as error:
            print(error)
    except requests.exceptions.HTTPError as error:
        print(error)
    except requests.ConnectionError as error:
        print(error)
