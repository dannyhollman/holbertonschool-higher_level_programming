#!/usr/bin/python3
def complex_delete(d, value):
    for k, v in list(d.items()):
        if v == value:
            del d[k]
    return d
