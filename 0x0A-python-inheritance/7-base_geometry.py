#!/usr/bin/python3
"""
Module for a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    a class BaseGeometry (based on 6-base_geometry.py).
    """

    def area(self):
        """
        a function that raises an Exception with the
        message area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        that validates value:
        you can assume name is always a string.

        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer.

        if value is less or equal to 0: raise a ValueError exception with
        the message <name> must be greater than 0
        """

        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
