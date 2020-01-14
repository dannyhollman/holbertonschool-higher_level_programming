#!/usr/bin/python3
""" sends a request to URL and displays body of response """
from urllib import request, error
from sys import argv


def main():
    """ sends a request to URL and displays body of response"""
    try:
        with request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    main()
