#!/usr/bin/python3
import sys


def main():
    total = 0
    for x in range(1, len(sys.argv)):
        total += int(sys.argv[x])
    print("{:d}".format(total))

if __name__ == "__main__":
    main()
