#!/usr/bin/python3
""" prints State object with name passed as argument """
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """ prints State object """
    engine = create_engine(
            'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == argv[4]).first()

    if result:
        print(result.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
