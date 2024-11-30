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

    if isinstance(obj, a_class):
        return True
    else:
        return False
