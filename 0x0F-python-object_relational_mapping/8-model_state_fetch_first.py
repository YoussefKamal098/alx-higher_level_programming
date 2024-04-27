#!/usr/bin/python3
"""
Module: main

This module initializes a database session, connects to a MySQL
database using provided credentials, and queries the first state from
the database.

It imports SQLAlchemy's create_engine, scoped_session, and sessionmaker to
establish a connection to the database, and imports the Base and State
classes from the model_state module.

Usage:
    Run this module with the following command-line arguments:
        python3 module_name.py <mysql_user> <mysql_password> <database_name>

    Example:
        python3 module_name.py username password my_database
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create a SQLAlchemy database engine
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:"
                           f"{mysql_password}@localhost:3306/{database_name}")

    # Create a scoped session with autoflush and autocommit disabled
    session = scoped_session(
        sessionmaker(
            autoflush=False,
            autocommit=False,
            bind=engine
        )
    )

    # Associate the Base class with the session's query property and
    # create all tables
    Base.query = session.query_property()
    Base.metadata.create_all(engine)

    # Query the first state from the database and print its ID and
    # name if it exists
    first_state = State.query.first()

    if first_state:
        print(first_state.id, first_state.name, sep=": ")
    else:
        print("Nothing")
