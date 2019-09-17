#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for x in my_list:
        if x % 2 == 0:
            new.append(1)
        else:
            new.append(0)
    return new
