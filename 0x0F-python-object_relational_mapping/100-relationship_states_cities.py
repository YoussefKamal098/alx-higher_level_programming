#!/usr/bin/python3
"""
This script adds a new State object "California" with
a linked City object "San Francisco" to the database.

Usage:
    python3 script_name.py [mysql_user] [mysql_password] [database_name]

Arguments:
    mysql_user (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Name of the MySQL database.

Module Description:
    This module connects to a MySQL database using the provided credentials.
    It creates a new State object "California" and
    a linked City object "San Francisco".
    The State and City objects are added to the database
    using the SQLAlchemy ORM.
    After adding the objects, the transaction is committed
    to save the changes to the database.
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from relationship_city import City
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
    engine = create_engine(connection_string)

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

    # Create a new State object "California" and
    # a linked City object "San Francisco"
    state = State(name="California")
    state.cities.append(City(name="San Francisco"))

    # Add the State and City objects to the session and commit the transaction
    session.add(state)
    session.commit()
