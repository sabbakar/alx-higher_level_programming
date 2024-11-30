#!/usr/bin/python3
"""
A module for  a function that returns True if
the object is an instance of a class that inherited (directly orindirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    A module for  a function that returns True if
    the object is an instance of a class that inherited (directly orindirectly)
    from the specified class ; otherwise False.
    """

    return issubclass(obj.__class__, a_class) and (type(obj) is not a_class)
