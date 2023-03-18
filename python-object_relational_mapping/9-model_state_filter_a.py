#!/usr/bin/python3
"""Script that lists all State objects that contain the letter 'a'"""

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

    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
