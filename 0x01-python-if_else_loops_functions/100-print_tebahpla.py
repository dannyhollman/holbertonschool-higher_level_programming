#!/usr/bin/python3
x = 122
i = 1
while x != 96:
    print("{}".format(chr(x)), end="")
    if i % 2 != 0:
        x -= 33
    else:
        x += 31
    i += 1
