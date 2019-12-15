#!/usr/bin/python3
""" changes the name of a State object """
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """ change name of a State """
    engine = create_engine(
            'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.id == 2).update(
            {State.name: 'New Mexico'})
    session.commit()


if __name__ == "__main__":
    main()
