#!/usr/bin/python3
"""
A module for a class Rectangle that defines a rectangle by:
(based on 1-rectangle.py)
"""


class Rectangle:
    """
     a class Rectangle that defines a rectangle by:
     (based on 1-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        """
        a function that defines a rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        a function to get the width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        a function to set the width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        a function to get the height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        a function to set the height
        """

        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")

        if value < 0:
            raise ValueError("heigth must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        A function that returns the area of the rectangle
        """

        return self.height * self.width

    def perimeter(self):
        """
        A function that returns the rectangle perimeter:
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)
