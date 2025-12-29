# Magdalena Galwa
# 30/12/2025
# Description:
# Final task:
#   Create a tool which will calculate straight-line distance between different cities based on coordinates:
#   1. User will provide two city names by console interface
#   2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
#   3. Return distance between cities in kilometers
#   Do not forgot that Earth is a sphere, so length of one degree is different.

class GUI:
    def __init__(self):
        # Show a welcome message and input options for the user
        print("=== Welcome to the Distance Calculator App! ===")
        print("=== Enter the names of two cities. The application will calculate the distance between them in kilometers. ===")
        self.city1_name = self.enter_city_name("first")
        self.city2_name = self.enter_city_name("second")
        self.coordinates1 = self.enter_coordinates(self.city1_name)
        self.coordinates2 = self.enter_coordinates(self.city2_name)

    def enter_city_name(self, order):
        # Prompt user for a city name (order: 'first' or 'second')
        while True:
            city_name = input(f"Enter {order} city name (all characters allowed): ")
            if city_name.strip() != "":
                print(f"You entered: {city_name}")
                return city_name
            else:
                print("Invalid input! City name cannot be empty. Please try again.")

    def enter_coordinates(self, city_name):
        # Prompt user for latitude and longitude for a given city
        while True:
            lat_input = input(f"Enter latitude for {city_name} (float, e.g., 52.2297): ")
            try:
                latitude = float(lat_input)
                latitude = round(latitude, 4)
                break
            except ValueError:
                print("Invalid input! Please enter a valid float value for latitude (e.g., 52.2297).")
        while True:
            lon_input = input(f"Enter longitude for {city_name} (float, e.g., 21.0122): ")
            try:
                longitude = float(lon_input)
                longitude = round(longitude, 4)
                break
            except ValueError:
                print("Invalid input! Please enter a valid float value for longitude (e.g., 21.0122).")
        print(f"You entered coordinates for {city_name}: ({latitude}, {longitude})")
        return (latitude, longitude)



