#!/usr/bin/python3
""" lists all states with a name starting with N """
import MySQLdb
from sys import argv


def main():
    """ lists states starting with N """
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states\
            WHERE states.name LIKE 'N%'\
            ORDER BY id ASC;")
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)


if __name__ == "__main__":
    main()
