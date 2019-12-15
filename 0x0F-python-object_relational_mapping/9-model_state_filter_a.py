#!/usr/bin/python3
""" lists all State objects that contain the letter a """
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """ lists all State objects that contain the letter a """
    engine = create_engine(
            'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name.like('%a%'))

    for row in result:
        print(str(row.id) + ': ' + str(row.name))


if __name__ == "__main__":
    main()
