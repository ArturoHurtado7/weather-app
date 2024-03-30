import requests
from src.constants import WEATHER_ENDPOINTS


def api_call(service: str, city: str, country: str) -> tuple[int, dict]:
    """
    Make a call to OpenWeather API
    """
    endpoint: str = WEATHER_ENDPOINTS[service](city, country)
    response = requests.get(endpoint)
    response_json = response.json()
    return response.status_code, response_json


def current_weather(city: str, country: str) -> tuple[int, dict]:
    """
    Get current weather from OpenWeather API
    """
    return api_call("current", city, country)


def forecast_weather(city: str, country: str) -> tuple[int, dict]:
    """
    Get forecast weather from OpenWeather API
    """
    return api_call("forecast", city, country)
