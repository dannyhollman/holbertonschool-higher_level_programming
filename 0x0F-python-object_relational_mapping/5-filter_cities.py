#!/usr/bin/python3
""" lists all states with a name starting with N """
import MySQLdb
from sys import argv


def main():
    """ lists states starting with N """
    my_list = []
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
            WHERE cities.state_id = (SELECT states.id FROM states\
            WHERE states.name = %s)", [argv[4]])
    for row in cursor.fetchall():
        my_list.append(row[0])
    print(", ".join(my_list))


if __name__ == "__main__":
    main()
