#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument, safe from MySQL injections.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name,
        charset="utf8"
    )

    # Create cursor object
    cursor = db.cursor()

    # Prepare SQL query using parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    try:
        # Execute the SQL query with parameter
        cursor.execute(query, (state_name,))
        # Fetch all rows
        rows = cursor.fetchall()
        # Print the results
        for row in rows:
            print(row)
    except Exception as e:
        print("Error:", e)

    # Close cursor and database connection
    cursor.close()
    db.close()
