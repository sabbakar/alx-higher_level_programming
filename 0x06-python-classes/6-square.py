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
        """if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        property method to retrieve
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method to set size with value parameter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        method to retrieve postion
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        method to set the postion
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            """
            could also say:
                    if not isinstance(value, tuple):
                        raise TypeError("position must be
                        a tuple of 2 positive integers")

                    if len(value) != 2:
                            raise TypeError("position must be
                            a tuple of 2 positive integers")

                    if not all(isinstance(num, int) and
                    num >= 0 for num in value):
                    raise TypeError("position must be a
                    tuple of 2 positive integers")
            """
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        a method to return area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        a method that prints in stdout the square
        with the character '#'
        """
        if self.__size == 0:
            print("")
            return
            
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
