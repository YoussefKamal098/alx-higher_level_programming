#!/usr/bin/python3
"""
Module: This module defines the State class for SQLAlchemy ORM.

The State class represents a state entity in a database. It is used to define
the structure and behavior of the "states" table in the database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class: Represents a state entity in a database.

    Attributes:
        id (int): The primary key identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
