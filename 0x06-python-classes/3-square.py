#!/usr/bin/python3

"""a class that creates a square"""


class Square:
    """the square class"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): The size of the square
        """

        self.__size = size

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)
