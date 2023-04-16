#!/usr/bin/python3
"""Write a python file that contains the class definition \
of a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""Import sqlalchemy"""

Base = declarative_base()
"""create a base class for ORM models"""


class State(Base):
    """
    A class that inherits from base
    Args:
        id: auto-generated, unique integer, can't be null
            primary key
        name: string with max 128 characters, can't be null
    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
