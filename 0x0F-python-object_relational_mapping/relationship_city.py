#!/usr/bin/python3
"""
This module defines the City class, which represents
a city entity in the database.

Attributes:
    - __tablename__: Name of the table in the database where
      City objects are stored.
    - id: An auto-generated, unique integer representing the
      primary key of the City table.
    - name: A string column with a maximum length of 128 characters,
      representing the name of the city.
    - state_id: An integer column representing the foreign key to
      the states table, specifying the state to which the city belongs.
    - state: A relationship attribute specifying the
      relationship between City and State objects.

Note:
    This module requires the SQLAlchemy library.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from relationship_state import Base


class City(Base):
    """Class representing a city entity in the database."""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer, ForeignKey("states.id", ondelete="CASCADE"), nullable=False)

    # Define relationship between City and State objects
    state = relationship("State", back_populates="cities")
