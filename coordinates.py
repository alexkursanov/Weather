from dataclasses import dataclass

@dataclass
class Coordinates:
  latitude: float
  longitude: float

def get_gps_coordinates() -> Coordinates:
  coordinates = Coordinates(latitude = 56.8519, longitude = 60.6122)
  return coordinates


if __name__ == "__main__":
    print(get_gps_coordinates())
