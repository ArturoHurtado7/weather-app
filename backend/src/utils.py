import datetime
from datetime import timezone

def general_data(input: dict, tz: datetime.timezone) -> dict:
    """
    Convert general data from OpenWeather API to a more readable format
    """
    sunrise = datetime.datetime.fromtimestamp(input['sys']['sunrise'], tz=timezone.utc)
    sunset = datetime.datetime.fromtimestamp(input['sys']['sunset'], tz=timezone.utc)
    general = {
        "location_name": f"{input['name']}, {input['sys']['country']}",
        "geo_coordinates": f"[{input['coord']['lat']}, {input['coord']['lon']}]",
        "sunrise": sunrise.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S"),
        "sunset": sunset.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S"),
    }
    return general


def weather_data(input: dict, tz: datetime.timezone) -> dict:
    """
    Convert weather data from OpenWeather API to a more readable format
    """
    metric_temp = input["main"]["temp"]
    imperial_temp = metric_to_imperial_temp(metric_temp)
    requested_time = datetime.datetime.fromtimestamp(input['dt'], tz=timezone.utc)
    weather = {
        "temperature": f"{metric_temp}°C ({imperial_temp}°F)",
        "wind": f"{input['wind']['speed']} m/s",
        "cloudiness": f"{input['clouds']['all']} %",
        "pressure": f"{input['main']['pressure']} hpa",
        "humidity": f"{input['main']['humidity']} %",
        "requested_time": requested_time.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S"),
    }
    return weather


def metric_to_imperial_temp(metric_temp: float) -> float:
    """
    Convert temperature from metric to imperial
    """
    imperial_temp = metric_temp * 9 / 5 + 32
    imperial_temp = float("{:.2f}".format(imperial_temp))
    return imperial_temp
