#!/usr/bin/python3

"""
Script to query and print the ID of a state with
a specified name from a MySQL database.

This script connects to a MySQL database and queries for
a state with a specified name.
The script takes MySQL credentials, database name,
and state name as command-line arguments.
It then establishes a connection to the MySQL database,
creates a scoped session with SQLAlchemy,
and queries the 'states' table for a state with
a name containing the letter 'a'.
If a matching state is found, it prints its ID. Otherwise,
it prints "Not found".

Usage:
    python3 script_name.py <mysql_user> <mysql_password> <database_name>
     <state_name>

Args:
    mysql_user (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Name of the MySQL database.
    state_name (str): Name of the state to search for.

Example:
    python3 script_name.py root password my_database California
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine to connect to MySQL database
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_password}"
                           f"@localhost:3306/{database_name}")

    # Create scoped session
    session = scoped_session(
        sessionmaker(
            autoflush=False,
            autocommit=False,
            bind=engine
        )
    )

    # Associate Base with the session's query property
    Base.query = session.query_property()

    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    # Query for a state with a name containing 'a'
    state = (
        State.query
        .filter(State.name.like(f"%{state_name}%"))
        .order_by(State.id)
        .first()
    )

    # Print the state's ID if found, otherwise print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")
