from weather_api_service import Weather
from weather_formatter import format_weather
from datetime import datetime


def save_weather(weather: Weather)-> None:
    now = datetime.now()
    with open('histore.txt', "a") as f:
        f.write(f"{now}\n{format_weather(weather)}\n\n")
