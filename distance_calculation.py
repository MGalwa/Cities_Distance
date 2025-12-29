# Magdalena Galwa
# 30/12/2025
# Description:
# Final task:
#   Create a tool which will calculate straight-line distance between different cities based on coordinates:
#   1. User will provide two city names by console interface
#   2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
#   3. Return distance between cities in kilometers
#   Do not forgot that Earth is a sphere, so length of one degree is different.

# distance_calculation.py
import math

class Calculator:
    def __init__(self, radius=6371):
        # Default Earth radius in kilometers
        self.radius = radius

    def haversine(self, coord1, coord2):
        """
        Calculates the great-circle distance between two points on the Earth.
        :param coord1: (lat1, lon1) - tuple with latitude and longitude of the first city
        :param coord2: (lat2, lon2) - tuple with latitude and longitude of the second city
        :return: distance in kilometers
        """
        lat1, lon1 = coord1
        lat2, lon2 = coord2

        # Convert degrees to radians
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = self.radius * c
        return distance