#!/usr/bin/python3
"""a script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    name = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(State).filter(State.name == (name, ))
    if user:
        print(user[0].id)
    else:
        print("Not found")
