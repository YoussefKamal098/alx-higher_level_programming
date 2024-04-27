# !usr/bin/python3
"""
Module: main

This module initializes a database session and retrieves state
information from the database.

It connects to a MySQL database using the provided credentials and
SQLAlchemy's `create_engine` function. A scoped session is then
created using SQLAlchemy's sessionmaker to manage database interactions.
The module defines a State class representing state entities in
the database and queries all states from the database,
printing their IDs and names.

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
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_password}"
                           f"@localhost:3306/{database_name}")

    # Create a scoped session with autoflush and autocommit disabled
    session = scoped_session(
        sessionmaker(
            autoflush=False,
            autocommit=False,
            bind=engine
        )
    )

    # Associate the Base class with the session's query
    # property and create all tables
    Base.query = session.query_property()
    Base.metadata.create_all(engine)

    # Query all states from the database and print their IDs and names
    for instance in State.query.order_by(State.id).all():
        print(instance.id, instance.name, sep=": ")
