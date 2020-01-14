#!/usr/bin/python3
""" sends a request to URL and displays value of X-Request-Id """
import requests
from sys import argv


def main():
    """ sends a request to URL and displays value of X-Request-Id """
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))

if __name__ == "__main__":
    main()
