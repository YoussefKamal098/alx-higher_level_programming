#!/usr/bin/python3

"""
Script to query and print states from a MySQL database.

This script connects to a MySQL database and queries for
states whose names contain the letter 'a'. The script takes MySQL
credentials and database name as command-line arguments.
It then establishes a connection to the MySQL database,
creates a scoped session with SQLAlchemy, and queries the 'states'
table for states containing the letter 'a'. Finally, it prints the IDs
and names of the matched states.

Usage:
    python3 script_name.py <mysql_user> <mysql_password> <database_name>

Args:
    mysql_user (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Name of the MySQL database.

Example:
    python3 script_name.py root password my_database
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Query for states containing 'a' and print their IDs and names
    matched_states = (
        State.query
        .filter(State.name.like("%a%"))
        .order_by(State.id)
    )

    for state in matched_states:
        print(state.id, state.name, sep=": ")
