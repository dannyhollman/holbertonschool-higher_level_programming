#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return None
    total = 0
    div = 0
    for x in my_list:
        total += (x[0] * x[1])
        div += x[1]
    return total / div
