#!/usr/bin/python3
""" lists all State objects from database hbtn_0e_6_usa """
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """ lists all state objects """
    engine = create_engine(
            'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all()

    for row in result:
        print(str(row.id) + ': ' + str(row.name))


if __name__ == "__main__":
    main()
