#!/usr/bin/python3

"""a class that creates a square"""


class Square:
    """the square class"""

    def __init__(self, size=0):
        """initialize a new square

        Args:
        size (int): the size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
