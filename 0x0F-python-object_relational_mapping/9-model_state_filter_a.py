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

    users = session.query(State).filter(State.name.contains(
        '%a%')).order_by(State.id).all()
    for user in users:
        print(user.id, user.name, sep=": ")
