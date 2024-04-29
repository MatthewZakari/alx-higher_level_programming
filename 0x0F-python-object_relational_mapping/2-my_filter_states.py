#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")

    # Create cursor
    cur = conn.cursor()

    # Construct SQL query with user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4])

    # Execute query
    cur.execute(query)

    # Fetch all results
    query_rows = cur.fetchall()

    # Display results
    for row in query_rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
