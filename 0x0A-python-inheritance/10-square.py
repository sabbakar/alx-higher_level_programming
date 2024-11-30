#!/usr/bin/python3
"""
A module for  a class Square that inherits from
Rectangle (9-rectangle.py):
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle (9-rectangle.py):
    """

    def __init__(self, size):
        """
        size initialization
        """

        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Computes the area of this geometry.

        Returns:
            int: The area of this geometry object.
        '''
        return self.__size * self.__size
