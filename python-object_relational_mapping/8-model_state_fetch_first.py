#!/usr/bin/python3
"""Script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_ob = session.query(State).order_by(State.id).first()

    if not state_ob:
        print("Nothing")
    else:
        print("{}: {}".format(state_ob.id, state_ob.name))

    session.close()
