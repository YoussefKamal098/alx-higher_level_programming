#!/usr/bin/python3
"""
This module defines the State class,
which represents a state entity in the database.

Attributes:
    - __tablename__: Name of the table in the database
      where State objects are stored.
    - id: An auto-generated, unique integer representing the
      primary key of the State table.
    - name: A string column with a maximum length of 128 characters,
      representing the name of the state.
    - cities: A relationship attribute specifying the
      relationship between State and City objects.

Note:
    This module requires the SQLAlchemy library.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """Class representing a state entity in the database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Define relationship between State and City objects
    cities = relationship("City", back_populates="state", passive_deletes=True)
