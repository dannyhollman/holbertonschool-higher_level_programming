#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    final = 0
    i = 0
    while (i < len(roman_string)):
        temp1 = roman.get(roman_string[i])
        if (i + 1 < len(roman_string)):
            temp2 = roman.get(roman_string[i + 1])
            if (temp1 >= temp2):
                final = final + temp1
                i = i + 1
            else:
                final = final + temp2 - temp1
                i = i + 2
        else:
            final = final + temp1
            i = i + 1
    return final
