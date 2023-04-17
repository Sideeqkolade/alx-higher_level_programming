#!/usr/bin/python3
"""a script that prints all City objects from
   the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    users = session.query(State.name, City.id, City.name).filter(
                        State.id == City.state_id).order_by(City.id).all()
    for user in users:
        print(f"{user.name}: ({user.id}) {user.name}")
    session.commit()
