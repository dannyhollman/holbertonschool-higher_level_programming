#!/usr/bin/python3
""" sends request to URL and displays the response """
import requests
from sys import argv


def main():
    """ sends request to URL and displays the response """
    r = requests.get(argv[1])
    if r.status_code == 200:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))

if __name__ == "__main__":
    main()
