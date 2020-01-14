#!/usr/bin/python3
""" displays X-Request-Id from URL """
from urllib import request
from sys import argv


def main():
    """ displays X-Request-Id from URL """
    with request.urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))

if __name__ == "__main__":
    main()
