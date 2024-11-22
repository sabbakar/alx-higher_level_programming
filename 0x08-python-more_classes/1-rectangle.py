#!/usr/bin/python3
"""
A module that defines a rectangle based on 0-rectangle.py
"""


class Rectangle:
    """
    a class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        a function to instantiate width and height
        :param width:
        :param height:
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        a function to get the witdh
        :return:
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        a function to set the witdh
        :param value:
        :return:
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__size = value

    @property
    def height(self):
        """
        a function to get the current height
        :return: the height of the class
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        a function to set the height
        :param value:
        :return:
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
