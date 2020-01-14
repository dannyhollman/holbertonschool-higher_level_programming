#!/usr/bin/python3
""" sends POST request to URL with email parameter, displays response """
import requests
from sys import argv


def main():
    """ sends POST request to URL with email parameter, displays response """
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)

if __name__ == "__main__":
    main()
