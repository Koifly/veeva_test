def get_lat_lon(location):
    return (location["lat"], location["lon"],)

def get_date(date_and_hour):
    date = date_and_hour.split()[0]
    return date

def get_rain(reading):
    #import pdb; pdb.set_trace()
    try:
        return reading["rain"]["3h"]
    except:
        return 0

def create_day_data(date, hi, lo, rain):
    day_data = {}
    day_data["date"] = date
    day_data["hi"] = hi
    day_data["lo"] = lo
    day_data["rain"] = rain

    return day_data

def parse_weather_data(weather_data):
    """Get daily weather from received data
    Get the date
    Get the high and low temperatures for each of the 5 days
    Get sum total precipitation there will be for each day
    If there won't be any precipitation for a particular day, return 0mm
    """
    readings = weather_data["list"]
    result = []
    day_data = {}

    for i, reading in enumerate(readings):
        islast = i == len(readings) - 1

        date = get_date(reading["dt_txt"])
        hi = reading["main"]["temp_max"]
        lo = reading["main"]["temp_min"]
        rain = get_rain(reading)
        if i == 0:
            day_data = create_day_data(date, hi, lo, rain)
        else:
            if date == day_data["date"]:
                day_data["hi"] = max(day_data["hi"], hi)
                day_data["lo"] = min(day_data["lo"], lo)
                day_data["rain"] += rain

                if islast:
                    result.append(day_data)

            else:
                result.append(day_data)
                day_data = create_day_data(date, hi, lo, rain)

                if islast:
                    result.append(day_data)

    return result