from weather_api_service import Weather

def format_weather(weather: Weather)-> str:
    return (f"Сегодня температура {weather.temperature} градусов цельсия, "
            f"{weather.weather_type}. \n"
            f"Ощущается как {weather.feels_like} градусов цельсия, "
            f"давление {weather.pressure * 0.750062:.2f} мм.рт.ст., "
            f"влажность {weather.humidity}%. \n"
            f"Восход {str(weather.sunrise.time())}, "
            f"закат {str(weather.sunset.time())}."
    )

if __name__ == "__main__":
    from datetime import datetime
    print(format_weather(Weather(temperature = 0.0,
                           feels_like = 0.0,
                           pressure = 0.0,
                           humidity = 0,
                           weather_type ='ясно',
                           sunrise = datetime.fromisoformat('2024-12-07 04:00:00'),
                           sunset = datetime.fromisoformat('2024-12-07 20:00:00'))
                   ))