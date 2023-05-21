import json
from . test_data import weather_response, parsed_weather_data
from .. data_processing import parse_weather_data

def test_parsing():
    json_data = json.loads(weather_response)
    result = parse_weather_data(json_data)
    assert parsed_weather_data == result
