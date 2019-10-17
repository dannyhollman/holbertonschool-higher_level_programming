#!/usr/bin/python3
"""adds all agruments to a python list and saves to file"""
import json
import sys


def save_to_json_file(my_obj, filename):
    """saves object to file"""
    with open(filename, "w") as f:
        j = json.dumps(my_obj)
        f.write(j)
        f.close()


def load_from_json_file(filename):
    """creates object"""
    with open(filename) as f:
        data = f.read()
        j = json.loads(data)
        return j


def main():
    """entry point"""
    try:
        load = load_from_json_file("add_item.json")
    except:
        load = []

    for x in range(1, len(sys.argv)):
        load.append(sys.argv[x])

    save_to_json_file(load, "add_item.json")

if __name__ == "__main__":
    main()
