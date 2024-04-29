#!/usr/bin/python3

"""
This script retrieves all City objects along with their
corresponding State names from the database.

Usage:
    python3 script_name.py [mysql_user] [mysql_password] [database_name]

Arguments:
    mysql_user (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Name of the MySQL database.

Module Description:
    This module connects to a MySQL database using the provided credentials.
    It retrieves all City objects along with their
    corresponding State names from the database.
    The retrieved data is printed in the format: "<city_id>:
    <city_name> -> <state_name>".
    The script uses SQLAlchemy for database interaction.

Requirements:
    - SQLAlchemy
    - MySQL server running on localhost

"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, joinedload

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

    # Retrieve cities with their corresponding state names
    cities = (
        City.query
        .join(City.state)
        .with_entities(City.id, City.name, State.name.label("state_name"))
        .order_by(City.id)
        .all()
    )

    # Print retrieved data
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state_name}")
