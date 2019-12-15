#!/usr/bin/python3
""" deletes all State objects with 'a' in name """
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """ deletes all State objects with 'a' in name """
    engine = create_engine(
            'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name.like('%a%'))

    for row in result:
        session.delete(row)

    session.commit()


if __name__ == "__main__":
    main()
