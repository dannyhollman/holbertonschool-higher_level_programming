#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    for x in names:
        if x[0] != '_':
            print(x)

if __name__ == "__main__":
    main()
