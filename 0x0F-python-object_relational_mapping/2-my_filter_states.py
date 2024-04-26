#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
import sys

import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_user,
                         passwd=mysql_password,
                         db=database_name
                         )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to retrieve the states with specific name
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
    cursor.execute(query.format(state_name))

    # Fetch all rows using fetchall() method
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    cursor.close()

    # Close the database connection
    db.close()
