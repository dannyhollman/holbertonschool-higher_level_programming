#!/usr/bin/python3
""" adds the State object 'Louisiana' """
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """ adds 'Louisiana' """
    engine = create_engine(
            'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    louisiana = State(name='Louisiana')
    session.add(louisiana)
    session.commit()

    print(louisiana.id)


if __name__ == "__main__":
    main()
