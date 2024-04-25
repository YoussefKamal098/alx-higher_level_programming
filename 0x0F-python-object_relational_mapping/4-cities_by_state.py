#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""
import sys

import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_user,
                         passwd=mysql_password,
                         db=database_name
                         )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to retrieve the all cities
    query = """
        SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states ON states.id=cities.state_id
        ORDER BY cities.id ASC
        """
    cursor.execute(query)

    # Fetch all rows using fetchall() method
    states = cursor.fetchall()
    # Print the results
    for state in states:
        print(state)

    cursor.close()

    # Close the database connection
    db.close()
