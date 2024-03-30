from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_weather_correct():
    city = "bogota"
    country = "co"
    url = f"/weather?city={city}&country={country}"
    response = client.get(url)
    response_json = response.json()
    assert response.status_code == 200
    assert "location_name" in response_json
    assert "geo_coordinates" in response_json
    assert "sunrise" in response_json
    assert "sunset" in response_json
    assert "temperature" in response_json
    assert "wind" in response_json
    assert "cloudiness" in response_json
    assert "pressure" in response_json
    assert "humidity" in response_json

def test_get_weather_city_not_found():
    city = "xxxxxxx"
    country = "co"
    url = f"/weather?city={city}&country={country}"
    response = client.get(url)
    assert response.status_code == 404

def test_get_weather_country_more_than_two():
    city = "bogota"
    country = "xxxx"
    url = f"/weather?city={city}&country={country}"
    response = client.get(url)
    assert response.status_code == 422

def test_get_weather_country_less_than_two():
    city = "bogota"
    country = "s"
    url = f"/weather?city={city}&country={country}"
    response = client.get(url)
    assert response.status_code == 422

def test_get_weather_city_empty():
    city = ""
    country = "co"
    url = f"/weather?city={city}&country={country}"
    response = client.get(url)
    assert response.status_code == 422

def test_get_weather_country_empty():
    city = "bogota"
    country = ""
    url = f"/weather?city={city}&country={country}"
    response = client.get(url)
    assert response.status_code == 422

def test_get_weather_city_country_empty():
    city = ""
    country = ""
    url = f"/weather?city={city}&country={country}"
    response = client.get(url)
    assert response.status_code == 422

def test_get_weather_city_country_none():
    url = f"/weather"
    response = client.get(url)
    assert response.status_code == 422

def test_get_weather_city_country_space():
    city = " "
    country = " "
    url = f"/weather?city={city}&country={country}"
    response = client.get(url)
    assert response.status_code == 422

def test_get_weather_cache():
    city = "barranquilla"
    country = "co"
    url = f"/weather?city={city}&country={country}"
    response = client.get(url)
    response_json = response.json()
    assert response.status_code == 200
    assert "from_cache" in response_json
    assert response_json["from_cache"] == False
    response = client.get(url)
    response_json = response.json()
    assert response.status_code == 200
    assert "from_cache" in response_json
    assert response_json["from_cache"] == True
