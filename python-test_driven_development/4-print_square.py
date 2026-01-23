#!/usr/bin/python3
"""
size is the size length of the square
size must be an integer,
otherwise raise a TypeError exception with the message size must be an integer
"""


def print_square(size):
    """
    Function that prints a square with the character #
    """
    if size == "":
        raise ValueError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
