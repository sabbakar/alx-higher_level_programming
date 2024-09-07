#!/usr/bin/python3
"""
A module that defines a square class by: (based on 4-square.py)
"""


class Square:
    """
    a square class
    """
    def __init__(self, size):
        """
        a method that instantiates size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        a method to define getter of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        a setter to set the size
        """
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        a method that returns the current area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        a method that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
