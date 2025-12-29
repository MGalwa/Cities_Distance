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
        print("=== Welcome to the Distance Calculator App! ===")  # Display welcome message
        print("=== Enter the names of two cities. The application will calculate the distance between them in kilometers. ===")  # Display instructions
        self.city1_name = self.enter_city_name("first")  # Ask user for the first city name and store it
        self.city2_name = self.enter_city_name("second")  # Ask user for the second city name and store it

    def enter_city_name(self, order):
        while True:  # Loop until a valid city name is entered
            city_name = input(f"Enter {order} city name (all characters allowed): ")  # Prompt user for city name
            if city_name.strip() != "":  # Check if input is not empty
                print(f"You entered: {city_name}")  # Confirm the entered city name
                return city_name  # Return the valid city name
            else:
                print("Invalid input! City name cannot be empty. Please try again.")  # Warn if input is empty

    def enter_coordinates(self, city_name):
        print("\nCoordinates must be within the following ranges:")  # Display coordinate instructions
        print("Latitude (φ):    from -90.0000° to +90.0000°")  # Latitude range info
        print("    0° is the Equator.")  # Equator info
        print("    Positive (+) values: Northern Hemisphere (N).")  # Positive latitude info
        print("    Negative (-) values: Southern Hemisphere (S).")  # Negative latitude info
        print("Longitude (λ):   from -180.0000° to +180.0000°")  # Longitude range info
        print("    0° is the Prime Meridian (Greenwich).")  # Prime Meridian info
        print("    Positive (+) values: Eastern Hemisphere (E).")  # Positive longitude info
        print("    Negative (-) values: Western Hemisphere (W).")  # Negative longitude info

        while True:  # Loop until a valid latitude is entered
            lat_input = input(f"Enter latitude for {city_name} (float, e.g., 52.2297): ")  # Prompt for latitude
            try:
                latitude = float(lat_input)  # Try to convert input to float
                if latitude < -90.0 or latitude > 90.0:  # Check latitude range
                    print("Latitude must be between -90.0000 and +90.0000 degrees.")  # Warn if out of range
                    continue  # Ask again
                latitude = round(latitude, 4)  # Round latitude to 4 decimal places
                break  # Exit loop if valid
            except ValueError:
                print("Invalid input! Please enter a valid float value for latitude (e.g., 52.2297).")  # Warn if not a float

        while True:  # Loop until a valid longitude is entered
            lon_input = input(f"Enter longitude for {city_name} (float, e.g., 21.0122): ")  # Prompt for longitude
            try:
                longitude = float(lon_input)  # Try to convert input to float
                if longitude < -180.0 or longitude > 180.0:  # Check longitude range
                    print("Longitude must be between -180.0000 and +180.0000 degrees.")  # Warn if out of range
                    continue  # Ask again
                longitude = round(longitude, 4)  # Round longitude to 4 decimal places
                break  # Exit loop if valid
            except ValueError:
                print("Invalid input! Please enter a valid float value for longitude (e.g., 21.0122).")  # Warn if not a float

        print(f"You entered coordinates for {city_name}: ({latitude}, {longitude})")  # Confirm entered coordinates
        return (latitude, longitude)  # Return coordinates as a tuple

    def print_summary(self, city1, coords1, city2, coords2, distance):
        print("\nSummary:")  # Print summary header
        print(f"City 1: {city1}, Coordinates: {coords1}")  # Print first city and its coordinates
        print(f"City 2: {city2}, Coordinates: {coords2}")  # Print second city and its coordinates
        print(f"Straight-line distance between {city1} and {city2}: {distance:.2f} km")  # Print calculated distance