from config import WEATHER_API_KEY


WEATHER_URL = "http://api.openweathermap.org/data/2.5"

WEATHER_ENDPOINTS = {
    "current": lambda city, country: (
        f"{WEATHER_URL}/weather?q={city},{country}&appid={WEATHER_API_KEY}&units=metric"
    ),
    "forecast": lambda city, country: (
        f"{WEATHER_URL}/forecast?q={city},{country}&appid={WEATHER_API_KEY}&units=metric"
    )
}

CACHE_HOLD_MINUTES = 2