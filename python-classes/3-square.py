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

    def __init__(self, size=0):
        """
        Initialize a square instance

        Args:
            size: The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Public instance method

        Returns:
            The current square area
        """
        return self.__size * self.size
