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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square instance

        Args:
            size: The size of the square
            position: absice and ordonate
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Private instance

        Retrieve the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position with validation
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("osition must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Public instance method

        Returns:
            The current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Public instance method

        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
