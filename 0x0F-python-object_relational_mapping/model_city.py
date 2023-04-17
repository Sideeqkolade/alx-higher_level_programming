#!/usr/bin/python3
"""a file that contains the class definition of a City"""

from sqlalchemy import Integer, Column, ForeignKey, String
from model_state import Base


class City(Base):
    """ 
    A class city that inherits from Base
    It links to the MySQL table cities
    Args:
        id: unique integer, auto generated, can't be null, primary key
        name: String, 128 characters, an't be null
        state_id: integer, can't be null, foreign key to states.id
    """

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
