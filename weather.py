from coordinates import get_gps_coordinates
from weather_api_service import get_wether
from weather_formatter import format_weather
from history import save_weather

def main():
    coordinates = get_gps_coordinates()
    weather = get_wether(coordinates)
    print(format_weather(weather))
    save_weather(weather)

if __name__ == "__main__":
    main()