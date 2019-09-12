#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) == 1:
        print("0 arguments.")
        exit()
    print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
