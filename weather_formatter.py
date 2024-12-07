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