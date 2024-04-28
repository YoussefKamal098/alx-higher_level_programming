#!/usr/bin/python3

"""
This module defines the City class representing a city in a SQLAlchemy model.

Module Description:
    The City class represents a city in the SQLAlchemy model. It defines the
    structure of the 'cities' table
    in the database, including columns for id, name, and state_id.
    The 'cities' table is related to the 'states' table through a
    foreign key constraint on the 'state_id' column.

Attributes:
    - id (int): The primary key of the city, unique and not nullable.
    - name (str): The name of the city, with a maximum length of 128 characters
      and not nullable.
    - state_id (int): The foreign key referencing the id of the corresponding
      state in the 'states' table.

Requirements:
    - SQLAlchemy
    - model_state module containing the Base class for declarative base
      and State class representing the state model.

"""

from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base


class City(Base):
    """
    City class representing a city in the SQLAlchemy model.

    Attributes:
        id (int): The primary key of the city, unique and not nullable.
        name (str): The name of the city, with a maximum length
        of 128 characters and not nullable.
        state_id (int): The foreign key referencing the id of the
        corresponding state in the 'states' table.

    Table Name:
        'cities'

    Foreign Key Relationship:
        The 'state_id' column references the 'id' column of the 'states' table.

    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
