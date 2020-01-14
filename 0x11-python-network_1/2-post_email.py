#!/usr/bin/python3
""" sends POST request to URL with email as parameter """
from urllib import request, parse
from sys import argv


def main():
    """ sends POST request to URL with email as parameter """
    data = parse.urlencode({'email': argv[2]}).encode()
    req = request.Request(argv[1], data=data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

if __name__ == "__main__":
    main()
