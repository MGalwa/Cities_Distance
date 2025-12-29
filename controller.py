# Magdalena Galwa
# 30/12/2025
# Description:
# Final task:
#   Create a tool which will calculate straight-line distance between different cities based on coordinates:
#   1. User will provide two city names by console interface
#   2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
#   3. Return distance between cities in kilometers
#   Do not forgot that Earth is a sphere, so length of one degree is different.

from view import GUI

if __name__ == "__main__":  # Main program entry point
    gui = GUI()

    city1 = gui.city1_name
    city2 = gui.city2_name
    coords1 = gui.coordinates1
    coords2 = gui.coordinates2

    print(f"\nSummary:")
    print(f"City 1: {city1}, Coordinates: {coords1}")
    print(f"City 2: {city2}, Coordinates: {coords2}")