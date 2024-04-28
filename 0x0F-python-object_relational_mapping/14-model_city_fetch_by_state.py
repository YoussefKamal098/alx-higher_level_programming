#!/usr/bin/python3

"""
This script fetches and prints all City objects with their
associated State names from the database hbtn_0e_14_usa.

Usage:
    python3 14-model_city_fetch_by_state.py
    [mysql_user] [mysql_password] [database_name]

Arguments:
    mysql_user (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Name of the MySQL database.

Module Description:
    This module connects to a MySQL database using the
    provided credentials.
    It queries the 'states' table and joins it with the
    'cities' table on the state_id foreign key.
    The script retrieves City objects along with their associated State names.
    Results are ordered by city ID and displayed with the state name.

Requirements:
    - SQLAlchemy
    - MySQL server running on localhost

"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from model_city import City
from model_state import Base, State

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
    Base.metadata.create_all(engine)

    # Query for all City objects with associated State names
    cities = (
        State.query
        .join(City, City.state_id == State.id)
        .with_entities(City.name, City.id, State.name.label("state_name"))
        .order_by(City.id)
    )

    # Print each city with its associated state name
    for city in cities:
        print(f"{city.state_name} : ({city.id}) {city.name}")
