#!/usr/bin/python3
""" uses the Github API to display id """
import requests
from sys import argv


def main():
    """ uses the Github API to display id """
    url = "https://api.github.com/user"
    try:
        response = requests.get(url, auth=(argv[1], argv[2])).json()
        print(response['id'])
    except:
        print('None')

if __name__ == "__main__":
    main()
