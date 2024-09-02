#!/usr/bin/python3
"""
a module to define a Square class with private size attribute.
"""


class Square:
    """
    a class to define a square with a private size attribute.
    """
    def __init__(self, size):
        """
        A method that initializes the square instance to accept size
        """
        self.__size = size
