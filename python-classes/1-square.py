#!/usr/bin/python3
"""
Module of a class that defines a square
"""


class Square:
    """
    Class that defines a square

    Attributes:
        __size: private size of the square
    """

    def __init__(self, size):
        """
        Initialize a square instance

        Args:
            size: The size of the square
        """
        self.__size = size
