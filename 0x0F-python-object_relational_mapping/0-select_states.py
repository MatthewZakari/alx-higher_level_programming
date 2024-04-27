#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    # Create cursor
    cur = conn.cursor()

    # Execute query to select all states sorted by id
    cur.execute("SELECT DISTINCT id, name FROM states GROUP BY id, name ORDER BY id ASC")

    # Fetch all rows
    query_rows = cur.fetchall()

    # Print results
    for row in query_rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
