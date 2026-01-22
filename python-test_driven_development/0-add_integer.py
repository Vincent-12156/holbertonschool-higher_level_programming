#!/usr/bin/python3
"""
Module of a function to add two integers
The function add_integer adds two numbers after validating
their types.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    """
    if a == "":
        raise ValueError("a must be an integer")
    elif not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
