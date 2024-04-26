#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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

    # Execute SQL query to retrieve the all cities
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id=states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id ASC
        """
    cursor.execute(query, (state_name,))

    # Fetch all rows using fetchall() method
    cities = list(row[0] for row in cursor.fetchall())

    # Print the results
    print(*cities, sep=", ")

    cursor.close()

    # Close the database connection
    db.close()
