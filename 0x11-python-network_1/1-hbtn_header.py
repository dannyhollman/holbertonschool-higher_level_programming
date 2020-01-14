#!/usr/bin/python3
""" displays X-Request-Id from URL """
from urllib import request
import sys


def main():
    """ displays X-Request-Id from URL """
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print(response.headers.get('X-Request-Id'))

if __name__ == "__main__":
    main()
