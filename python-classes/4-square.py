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
        self.__size = size

    @property
    def size(self):
        """
        Retrieve size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """
        Set the new_size

        Args:
            new_size: New_size of the square
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def area(self):
        """
        Public instance method

        Returns:
            The current square area
        """
        return self.__size * self.size
