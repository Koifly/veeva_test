import json
import unittest
import nose
from test_data import weather_response, parsed_weather_data
from weather import parse_weather_data

def test_parsing():
    json_data = json.loads(weather_response)
    result = parse_weather_data(json_data)
    nose.tools.eq_(parsed_weather_data, result, msg=None)

test_parsing()