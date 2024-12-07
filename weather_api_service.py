from dataclasses import dataclass
import urllib.request
import json
from typing_extensions import TypeAlias
from datetime import datetime

from coordinates import Coordinates
import config

Celsius: TypeAlias = float

@dataclass
class Weather:
  temperature: Celsius
  feels_like: float
  pressure: float
  humidity: int
  weather_type: str
  sunrise: datetime
  sunset: datetime

def get_wether(coordinates: Coordinates) -> Weather:
    openweather_response = _get_openweather_response(latitude = coordinates.latitude,
                                                    longitude = coordinates.longitude)
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response(latitude: float, longitude: float):
    return urllib.request.urlopen(
        config.OPENWEATHER_URL.format(latitude=latitude, longitude=longitude)).read()


def _parse_openweather_response(openweather_response)-> Weather:
    weather_from_api_dict = json.loads(openweather_response)
    weather_type = weather_from_api_dict['weather'][0]['description']
    feels_like = weather_from_api_dict['main']['feels_like']
    pressure = weather_from_api_dict['main']['pressure'] * 0.750062
    humidity = weather_from_api_dict['main']['humidity']
    sunrise = datetime.fromtimestamp(weather_from_api_dict['sys']['sunrise'])
    sunset = datetime.fromtimestamp(weather_from_api_dict['sys']['sunset'])
    return Weather(temperature=_parse_temperature(weather_from_api_dict),
                   weather_type=weather_type,
                   feels_like=feels_like,
                   pressure=pressure,
                   humidity=humidity,
                   sunrise=sunrise,
                   sunset=sunset)

def _parse_temperature(openweather_dict: dict) -> Celsius:
    return openweather_dict['main']['temp']



if __name__ == "__main__":
    print(get_wether(Coordinates(latitude=50.0, longitude=33.0)))