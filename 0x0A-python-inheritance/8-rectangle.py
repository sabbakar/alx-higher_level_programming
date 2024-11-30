#!/usr/bin/python3
"""
A module for a class Rectangle that inherits Based
on BaseGeometry (7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class Rectangle that inherits based on BaseGeometry (7-base_geometry.py)
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height
        """

        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
