#!/usr/bin/python3
""" lists all states in the database """
import MySQLdb
from sys import argv


def main():
    """ Connect to database, select state and id """
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC;")
    for row in cursor.fetchall():
        print(row)


if __name__ == "__main__":
    main()
