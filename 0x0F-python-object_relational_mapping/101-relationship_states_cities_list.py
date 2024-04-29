#!/usr/bin/python3

"""
This script retrieves data from the database using SQLAlchemy ORM.

Usage:
    python3 script_name.py [mysql_user] [mysql_password] [database_name]

Arguments:
    mysql_user (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Name of the MySQL database.

Module Description:
    This module connects to a MySQL database using the provided credentials.
    It queries the database for all states along with their associated cities.
    It uses SQLAlchemy's joinedload feature to eagerly load
    the cities along with states.
    The retrieved data is printed to the console.

Requirements:
    - SQLAlchemy
    - MySQL server running on localhost

"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, joinedload

from relationship_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create MySQL connection string
    connection_string = f"mysql+mysqldb://{mysql_user}:{mysql_password}" \
                        f"@localhost:3306/{database_name}"

    # Create SQLAlchemy engine
    engine = create_engine(connection_string, echo=True)

    # Create a scoped session
    session = scoped_session(
        sessionmaker(
            autoflush=False,
            autocommit=False,
            bind=engine
        )
    )

    # Set query property on Base
    Base.query = session.query_property()

    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    # Retrieve states along with their associated cities using joinedload
    states = (
        State.query
        .options(joinedload(State.cities))
        .order_by(State.id)
        .all()
    )

    # Print retrieved data
    for state in states:
        print(state.id, state.name, sep=": ")
        for city in state.cities:
            print("    ", end="")
            print(city.id, city.name, sep=": ")
