#!/usr/bin/python3
"""
Module that handle datas for a rectangle
"""


class Rectangle:
    """
    Defines a rectangle

    Attritubes:
        width: width of the rectanble
        Height: Height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialization

        Args:
            width: 0 defaut
            height: 0 defaut
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width with validation
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height with validation
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method

        Returns:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        String to print the rectangle with the character #
        """
        if self.__width == 0 or self.height == 0:
            return ""

        line = []
        for i in range(self.__height):
            line.append("#" * self.__width)

        return "\n".join(line)

    def __repr__(self):
        """
        Return a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
