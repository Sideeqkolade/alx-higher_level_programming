#!/usr/bin/python3
"""a script that lists all State objects from the
database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(State).order_by(State.id).first()
    if user:
        print(user.id, user.name, sep=": ")
    else:
        print("Nothing")
