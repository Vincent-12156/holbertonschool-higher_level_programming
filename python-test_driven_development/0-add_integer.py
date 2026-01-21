#!/usr/bin/python3
"""
Module of a function to add two integers
    :param a: must be an integer
    :param b: must be an integer
"""


def add_integer(a, b=98):
    """
    Docstring for add_integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
