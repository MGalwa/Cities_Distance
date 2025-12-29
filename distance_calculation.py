# distance_calculation.py
import math  # Import the math module for mathematical functions

class Calculator:
    def __init__(self, radius=6371):
        # Default Earth radius in kilometers
        self.radius = radius  # Store the radius value

    def haversine(self, coord1, coord2):
        """
        Calculates the great-circle distance between two points on the Earth.
        :param coord1: (lat1, lon1) - tuple with latitude and longitude of the first city
        :param coord2: (lat2, lon2) - tuple with latitude and longitude of the second city
        :return: distance in kilometers
        """
        lat1, lon1 = coord1  # Unpack the first city's coordinates
        lat2, lon2 = coord2  # Unpack the second city's coordinates

        # Convert degrees to radians
        lat1 = math.radians(lat1)  # Convert latitude of first city to radians
        lon1 = math.radians(lon1)  # Convert longitude of first city to radians
        lat2 = math.radians(lat2)  # Convert latitude of second city to radians
        lon2 = math.radians(lon2)  # Convert longitude of second city to radians

        dlat = lat2 - lat1  # Calculate the difference in latitude
        dlon = lon2 - lon1  # Calculate the difference in longitude

        # Apply the haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2  # Haversine formula part a
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))  # Haversine formula part c

        distance = self.radius * c  # Calculate the distance using the Earth's radius
        return distance  # Return the calculated distance in kilometers