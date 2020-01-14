#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """
import requests


def main():
    """ fetches https://intranet.hbtn.io/status """
    html = requests.get('https://intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))

if __name__ == "__main__":
    main()
