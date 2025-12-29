# Magdalena Galwa
# 30/12/2025
# Description:
# Final task:
#   Create a tool which will calculate straight-line distance between different cities based on coordinates:
#   1. User will provide two city names by console interface
#   2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
#   3. Return distance between cities in kilometers
#   Do not forgot that Earth is a sphere, so length of one degree is different.

# Import the database connection module
import db_connection
# Import the Calculator class for distance calculation
from distance_calculation import Calculator
# Import the GUI class for user interaction
from view import GUI

# Check if this script is being run as the main program
if __name__ == "__main__":
    gui = GUI()  # Create a GUI object to handle user input
    calculator = Calculator()  # Create a Calculator object for distance calculation
    DB = db_connection.DBConnection('Coordinates.db')  # Create a database connection to 'Coordinates.db'
    DB.create_city_coordinates_table()  # Create the city coordinates table if it does not exist

    city1 = gui.city1_name.strip().lower()  # Get the first city name, remove whitespace, and convert to lowercase
    city2 = gui.city2_name.strip().lower()  # Get the second city name, remove whitespace, and convert to lowercase

    # Handle the first city
    if not DB.city_exists(city1):  # If the first city does not exist in the database
        coords1 = gui.enter_coordinates(city1)  # Ask the user for coordinates of the first city
        DB.insert_city_coordinates(city1, coords1[0], coords1[1])  # Insert the first city and its coordinates into the database
    else:
        coords1 = DB.get_city_coordinates(city1)  # Get the coordinates of the first city from the database

    # Handle the second city
    if not DB.city_exists(city2):  # If the second city does not exist in the database
        coords2 = gui.enter_coordinates(city2)  # Ask the user for coordinates of the second city
        DB.insert_city_coordinates(city2, coords2[0], coords2[1])  # Insert the second city and its coordinates into the database
    else:
        coords2 = DB.get_city_coordinates(city2)  # Get the coordinates of the second city from the database

    distance = calculator.haversine(coords1, coords2)  # Calculate the straight-line distance between the two cities
    gui.print_summary(city1, coords1, city2, coords2, distance)  # Print a summary including the distance

    DB.print_all_cities()  # Print all cities and their coordinates from the database
    # DB.clear_city_coordinates_table()  # (Optional) Clear all records from the city coordinates table (commented out)