#!/usr/bin/python3
"""
A module that defines a qare xlass
"""


class Square:
    """
    a square class that defines a square by:
    (based on 5-square.py)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        a method that initializes optional size with
        optional position
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
