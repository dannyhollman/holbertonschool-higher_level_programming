#!/usr/bin/python3
"""indent text with newline"""


def text_indentation(text):
    """indent text"""
    indent = ".?:"
    final = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for x in range(len(text)):
        if text[x - 1] in indent:
            final += "\n\n"
        else:
            final += text[x]
    print(final, end="")
