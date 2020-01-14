#!/usr/bin/python3
""" sends a search request to the Star Wars API """
import requests
from sys import argv


def main():
    """ sends a search request to the Star Wars API """
    url = "https://swapi.co/api/people/?search="
    r = requests.get('{}{}'.format(url, argv[1])).json()
    print('Number of results: {}'.format(r['count']))
    for results in r['results']:
        print(results['name'])

if __name__ == "__main__":
    main()
