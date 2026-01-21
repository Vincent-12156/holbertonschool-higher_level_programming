#!/usr/bin/python3
"""
Module of a function to add two integers
The function add_integer adds two numbers after validating
their types.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    a (int or float): first number
    b (int or float): second number, defaults to 98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
