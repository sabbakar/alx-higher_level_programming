#!/usr/bin/python3
"""
A module that defines a square class
"""


class Square:
    """
    a class Square that defines a square by: 
    (based on 3-square.py)
    """
    def __init__(self, size=0):
        """
        a method of Private instance attribute: size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    @property
    def size(self):
        """
        a getter method to retrieve the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        a setter method to set a size
        """
	if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        method that returns the current square area
        """
        return self.__size * self.__size
