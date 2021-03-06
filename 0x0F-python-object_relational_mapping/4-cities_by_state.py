#!/usr/bin/python3
""" lists all states with a name starting with N """
import MySQLdb
from sys import argv


def main():
    """ lists states starting with N """
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC;")
    for row in cursor.fetchall():
        print(row)


if __name__ == "__main__":
    main()
