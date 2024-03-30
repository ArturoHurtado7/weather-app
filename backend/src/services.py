import datetime

from src.api import current_weather, forecast_weather
from src.utils import general_data, weather_data
from src.crud import get_cache, upsert_cache


def weather_service(city, country, db) -> tuple[int, dict]:
    """
    Get city weather, from cache database or from weather api
    """
    # Cache query
    cache_id = f"{city},{country}"
    cache = get_cache(db, cache_id)
    if cache:
        response = dict(cache.data) # type: ignore
        response["from_cache"] = True # type: ignore
        return 200, response 

    # API calls
    status_code, current_data = current_weather(city, country)
    if status_code != 200:
        return status_code, current_data

    status_code, forecast_data = forecast_weather(city, country)
    if status_code != 200:
        return status_code, forecast_data
    
    timezone = current_data.get("timezone")
    if timezone is None:
        tz = datetime.timezone.utc
    else:
        tz = datetime.timezone(datetime.timedelta(seconds=timezone))

    response = general_data(current_data, tz)
    response = response | weather_data(current_data, tz)
    response["forecast"] = [weather_data(item, tz) for item in forecast_data["list"]]
    response["from_cache"] = False

    upsert_cache(db, cache_id, response)
    return status_code, response
