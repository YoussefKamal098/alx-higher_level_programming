#!/usr/bin/python3

"""
This script deletes states from the database whose names
contain the letter 'a' using SQLAlchemy ORM.

Usage:
    python3 script_name.py [mysql_user] [mysql_password] [database_name]

Arguments:
    mysql_user (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Name of the MySQL database.

Module Description:
    This module connects to a MySQL database using the provided credentials.
    It then queries for states in the 'states' table whose names
    contain the letter 'a'.
    For each matching state, it deletes the record from the
    database using the SQLAlchemy ORM.
    After deleting the states, it commits the transaction to
    save the changes to the database.

Requirements:
    - SQLAlchemy
    - MySQL server running on localhost

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

    # Query for states whose names contain the letter 'a'
    states = (
        State.query
        .filter(State.name.like("%a%"))
    )

    # Delete the matching states from the database
    for state in states:
        session.delete(state)

    # Commit the transaction to save the changes to the database
    session.commit()
