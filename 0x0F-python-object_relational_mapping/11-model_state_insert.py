#!/usr/bin/python3
"""
This script adds a new state to the database using SQLAlchemy ORM.

Usage:
    python3 script_name.py [mysql_user] [mysql_password] [database_name]

Arguments:
    mysql_user (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Name of the MySQL database.

Module Description:
    This module connects to a MySQL database using the provided credentials.
    It then creates a new state entry in the 'states' table of
    the specified database using the SQLAlchemy ORM.
    After adding the new state, it prints the ID of the newly created state.

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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the transaction to save the new state to the database
    session.commit()

    # Print the ID of the newly created state
    print(new_state.id)
