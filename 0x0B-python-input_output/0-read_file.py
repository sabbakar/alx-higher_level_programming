#!/usr/bin/python3
"""module read file"""


def read_file(filename=""):
    """
    function to read file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
