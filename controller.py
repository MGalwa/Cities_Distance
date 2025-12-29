# Magdalena Galwa
# 30/12/2025
# Description:
# Final task:
#   Create a tool which will calculate straight-line distance between different cities based on coordinates:
#   1. User will provide two city names by console interface
#   2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
#   3. Return distance between cities in kilometers
#   Do not forgot that Earth is a sphere, so length of one degree is different.
# main.py
import db_connection
from distance_calculation import Calculator
from view import GUI

if __name__ == "__main__":
    gui = GUI()
    calculator = Calculator()
    DB = db_connection.DBConnection('Coordinates.db')
    DB.create_city_coordinates_table()

    city1 = gui.city1_name.strip().lower()
    city2 = gui.city2_name.strip().lower()

    # Handle first city
    if not DB.city_exists(city1):
        coords1 = gui.enter_coordinates(city1)
        DB.insert_city_coordinates(city1, coords1[0], coords1[1])
    else:
        coords1 = DB.get_city_coordinates(city1)

    # Handle second city
    if not DB.city_exists(city2):
        coords2 = gui.enter_coordinates(city2)
        DB.insert_city_coordinates(city2, coords2[0], coords2[1])
    else:
        coords2 = DB.get_city_coordinates(city2)

    distance = calculator.haversine(coords1, coords2)
    gui.print_summary(city1, coords1, city2, coords2, distance)

    DB.print_all_cities()