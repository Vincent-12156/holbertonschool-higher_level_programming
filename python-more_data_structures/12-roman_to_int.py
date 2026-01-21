#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    prec = 0
    result = 0

    for c in reversed(roman_string):
        value = convert.get(c, 0)
        if value < prec:
            result -= value
        else:
            result += value
            prec = value

    return result
