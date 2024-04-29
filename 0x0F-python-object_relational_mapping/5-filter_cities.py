#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database_name)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to fetch cities of the specified state
    sql_query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id ASC"

    try:
        # Execute the SQL query
        cursor.execute(sql_query, (state_name,))
        # Fetch all the rows in a list of tuples
        cities = cursor.fetchall()

        # Print the cities
        print(", ".join([city[0] for city in cities]))

    except Exception as e:
        print("Error:", e)

    finally:
        # Disconnect from server
        cursor.close()
        db.close()

