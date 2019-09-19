#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    for x in my_list:
        if x not in new:
            new.append(x)
    return sum(new)
