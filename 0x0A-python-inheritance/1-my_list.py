#!/usr/bin/python3
"""
A module fo  a class MyList that inherits from list
"""


class MyList(list):
    """
    a class MyList that inherits from list
    """

    def print_sorted(self):
        """
        function  that prints the list,
        but sorted (ascending sort)
        """

        print(sorted(self))
