import geocoder
from dataclasses import dataclass

@dataclass
class Coordinates:
  latitude: float
  longitude: float

def get_gps_coordinates() -> Coordinates:
  coordinates = Coordinates(latitude = 56.8519, longitude = 60.6122)
  #coordinates1 = _get_geocoder_coordinates()
  return coordinates

# def _get_geocoder_coordinates() -> Coordinates:
#     g = geocoder.google('Mountain View, CA')
#     print(g)
#
#     return 0 #Coordinates(latitude = g.latlng[0], longitude = g.latlng[1])

if __name__ == "__main__":
    print(get_gps_coordinates())
