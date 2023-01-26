#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """initialize a new square

        Args:
            size (int): the size of the square

        """
        self.size = size

    def area(self):
        """class method that gets the area of square

        Returns:
            result
        """
        result = self.__size * self.__size
        return (result)

    @property
    def size(self):
        """class method that retrieve a private instance attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ class method that prints a square"""
        if (self.__size == 0):
            print("")
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print("")
