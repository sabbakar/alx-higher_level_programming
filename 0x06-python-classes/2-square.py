#!/usr/bin/python3
"""
A Module that defines a Square class with
Private instance attribute: size
"""


class Square:
    """
    A class the defines square with Private instance attribute: size
    and Instantiation with optional size: def __init__(self, size=0):
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)
