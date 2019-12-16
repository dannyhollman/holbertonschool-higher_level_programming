#!/usr/bin/python3
""" prints all City objects """
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """ prints all City objects """
    engine = create_engine(
            'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State, City).filter(City.state_id == State.id).all()

    for state, city in result:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))


if __name__ == "__main__":
    main()
