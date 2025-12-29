# Magdalena Galwa
# 30/12/2025
# Description:
# Final task:
#   Create a tool which will calculate straight-line distance between different cities based on coordinates:
#   1. User will provide two city names by console interface
#   2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
#   3. Return distance between cities in kilometers
#   Do not forgot that Earth is a sphere, so length of one degree is different.

# db_connection.py
# db_connection.py
import sqlite3  # Import sqlite3 for database operations

class DBConnection:
    def __init__(self, db_name):
        self.db_name = db_name  # Store the database name
        self.conn = sqlite3.connect(self.db_name)  # Connect to the SQLite database file
        self.cursor = self.conn.cursor()  # Create a cursor for executing SQL commands

    def create_city_coordinates_table(self):
        """
        Create a table for storing city coordinates if it does not exist.
        Columns: id, city (unique), latitude, longitude
        """
        table_sql = '''
        CREATE TABLE IF NOT EXISTS CityCoordinates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique ID for each record
            city TEXT NOT NULL UNIQUE,             # City name (unique)
            latitude REAL NOT NULL,                # Latitude (float)
            longitude REAL NOT NULL                # Longitude (float)
        )
        '''
        self.cursor.execute(table_sql)  # Execute the SQL to create the table
        self.conn.commit()  # Commit the changes to the database

    def city_exists(self, city):
        sql = "SELECT 1 FROM CityCoordinates WHERE LOWER(city) = LOWER(?) LIMIT 1"  # SQL to check if city exists (case-insensitive)
        self.cursor.execute(sql, (city.strip(),))  # Execute the query with the city name
        return 1 if self.cursor.fetchone() is not None else 0  # Return 1 if found, 0 otherwise

    def insert_city_coordinates(self, city, latitude, longitude):
        city = city.strip()  # Remove leading/trailing whitespace from city name
        if self.city_exists(city):  # Check if city already exists in the database
            print(f"City '{city}' already exists in the database.")  # Inform user if city exists
            return False  # Return False if city exists
        sql = "INSERT INTO CityCoordinates (city, latitude, longitude) VALUES (?, ?, ?)"  # SQL to insert new city
        self.cursor.execute(sql, (city, latitude, longitude))  # Execute the insert command
        self.conn.commit()  # Commit the changes to the database
        print(f"City '{city}' with coordinates ({latitude}, {longitude}) added successfully.")  # Inform user of success
        return True  # Return True if insert was successful

    def print_all_cities(self):
        print(f"\nDB data with city coordinates:")  # Print header
        sql = "SELECT id, city, latitude, longitude FROM CityCoordinates"  # SQL to select all cities
        self.cursor.execute(sql)  # Execute the query
        rows = self.cursor.fetchall()  # Fetch all results
        if not rows:  # If there are no cities in the database
            print("No cities in the database.")  # Inform user
        else:
            print("All cities in the database:")  # Print header
            for row in rows:  # Loop through each city
                print(f"ID: {row[0]}, City: {row[1]}, Latitude: {row[2]}, Longitude: {row[3]}")  # Print city details

    def get_city_coordinates(self, city):
        sql = "SELECT latitude, longitude FROM CityCoordinates WHERE LOWER(city) = LOWER(?)"  # SQL to get coordinates (case-insensitive)
        self.cursor.execute(sql, (city.strip(),))  # Execute the query with the city name
        result = self.cursor.fetchone()  # Fetch the result
        if result:  # If city was found
            return (result[0], result[1])  # Return latitude and longitude as a tuple
        else:
            return None  # Return None if city not found

    def clear_city_coordinates_table(self):
        sql = "DELETE FROM CityCoordinates"  # SQL to delete all records from the table
        self.cursor.execute(sql)  # Execute the delete command
        self.conn.commit()  # Commit the changes to the database
        print("All records from CityCoordinates table have been deleted.")  # Inform user

