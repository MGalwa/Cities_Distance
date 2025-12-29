# Magdalena Galwa
# 30/12/2025
# Description:
# Final task:
#   Create a tool which will calculate straight-line distance between different cities based on coordinates:
#   1. User will provide two city names by console interface
#   2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
#   3. Return distance between cities in kilometers
#   Do not forgot that Earth is a sphere, so length of one degree is different.

# view.py
class GUI:
    def __init__(self):
        print("=== Welcome to the Distance Calculator App! ===")
        print("=== Enter the names of two cities. The application will calculate the distance between them in kilometers. ===")
        self.city1_name = self.enter_city_name("first")
        self.city2_name = self.enter_city_name("second")
        self.coordinates1 = self.enter_coordinates(self.city1_name)
        self.coordinates2 = self.enter_coordinates(self.city2_name)

    def enter_city_name(self, order):
        while True:
            city_name = input(f"Enter {order} city name (all characters allowed): ")
            if city_name.strip() != "":
                print(f"You entered: {city_name}")
                return city_name
            else:
                print("Invalid input! City name cannot be empty. Please try again.")

    def enter_coordinates(self, city_name):
        print("\nCoordinates must be within the following ranges:")
        print("Latitude (φ):    from -90.0000° to +90.0000°")
        print("    0° is the Equator.")
        print("    Positive (+) values: Northern Hemisphere (N).")
        print("    Negative (-) values: Southern Hemisphere (S).")
        print("Longitude (λ):   from -180.0000° to +180.0000°")
        print("    0° is the Prime Meridian (Greenwich).")
        print("    Positive (+) values: Eastern Hemisphere (E).")
        print("    Negative (-) values: Western Hemisphere (W).")

        while True:
            lat_input = input(f"Enter latitude for {city_name} (float, e.g., 52.2297): ")
            try:
                latitude = float(lat_input)
                if latitude < -90.0 or latitude > 90.0:
                    print("Latitude must be between -90.0000 and +90.0000 degrees.")
                    continue
                latitude = round(latitude, 4)
                break
            except ValueError:
                print("Invalid input! Please enter a valid float value for latitude (e.g., 52.2297).")

        while True:
            lon_input = input(f"Enter longitude for {city_name} (float, e.g., 21.0122): ")
            try:
                longitude = float(lon_input)
                if longitude < -180.0 or longitude > 180.0:
                    print("Longitude must be between -180.0000 and +180.0000 degrees.")
                    continue
                longitude = round(longitude, 4)
                break
            except ValueError:
                print("Invalid input! Please enter a valid float value for longitude (e.g., 21.0122).")

        print(f"You entered coordinates for {city_name}: ({latitude}, {longitude})")
        return (latitude, longitude)

    def print_summary(self, city1, coords1, city2, coords2, distance):
        print("\nSummary:")
        print(f"City 1: {city1}, Coordinates: {coords1}")
        print(f"City 2: {city2}, Coordinates: {coords2}")
        print(f"Straight-line distance between {city1} and {city2}: {distance:.2f} km")



