#!/usr/bin/python3
"""
A module that defines a class Square
"""


class Square:
    """
    a Square class that defines a square by:
    private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    """
    def __init__(self, size=0):
        """
        a method that defines the parameter of the square class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Public instance method: def area(self): that returns
        the current square area
        """
        a = self.__size * self.__size
        return a
