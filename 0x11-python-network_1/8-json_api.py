#!/usr/bin/python3
""" sends POST request with letter as prameter """
import requests
from sys import argv


def main():
    """ sends POST request with letter as prameter """
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    try:
        response = requests.post(url, data={'q': letter}).json()
        if "id" not in response or "name" not in response:
            print("No result")
        else:
            print("[{}] {}".format(response['id'], response['name']))
    except:
        print('Not a valid JSON')


if __name__ == "__main__":
    main()
