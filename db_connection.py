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
import sqlite3  # Import sqlite3 for database operations

class DBConnection:
    def __init__(self, db_name):
        self.db_name = db_name  # Store the database name
        self.conn = sqlite3.connect(self.db_name)  # Connect to the SQLite database
        self.cursor = self.conn.cursor()  # Create a cursor for executing SQL commands

    def create_city_coordinates_table(self):
        """
        Create a table for storing city coordinates if it does not exist.
        Columns: id, city (unique), latitude, longitude
        """
        table_sql = '''
        CREATE TABLE IF NOT EXISTS CityCoordinates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL UNIQUE,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL
        )
        '''
        self.cursor.execute(table_sql)
        self.conn.commit()

    def city_exists(self, city):
        sql = "SELECT 1 FROM CityCoordinates WHERE LOWER(city) = LOWER(?) LIMIT 1"
        self.cursor.execute(sql, (city.strip(),))
        return 1 if self.cursor.fetchone() is not None else 0

    def insert_city_coordinates(self, city, latitude, longitude):
        city = city.strip()
        if self.city_exists(city):
            print(f"City '{city}' already exists in the database.")
            return False
        sql = "INSERT INTO CityCoordinates (city, latitude, longitude) VALUES (?, ?, ?)"
        self.cursor.execute(sql, (city, latitude, longitude))
        self.conn.commit()
        print(f"City '{city}' with coordinates ({latitude}, {longitude}) added successfully.")
        return True

    def print_all_cities(self):
        print(f"\nDB data with city coordinates:")
        sql = "SELECT id, city, latitude, longitude FROM CityCoordinates"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        if not rows:
            print("No cities in the database.")
        else:
            print("All cities in the database:")
            for row in rows:
                print(f"ID: {row[0]}, City: {row[1]}, Latitude: {row[2]}, Longitude: {row[3]}")

    def get_city_coordinates(self, city):
        sql = "SELECT latitude, longitude FROM CityCoordinates WHERE LOWER(city) = LOWER(?)"
        self.cursor.execute(sql, (city.strip(),))
        result = self.cursor.fetchone()
        if result:
            return (result[0], result[1])
        else:
            return None

    def clear_city_coordinates_table(self):
        sql = "DELETE FROM CityCoordinates"
        self.cursor.execute(sql)
        self.conn.commit()
        print("All records from CityCoordinates table have been deleted.")

