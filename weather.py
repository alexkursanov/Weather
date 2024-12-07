
def main():
    coordinates = get_gps_coordinates()
    weather = get_wether(coordinates)
    print(format_weather(weather))
    save_weather(weather)

if __name__ == "__main__":
    main()