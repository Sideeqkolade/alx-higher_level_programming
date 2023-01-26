#!/usr/bin/python3

"""a class that creates a square"""


class Square:
    """the square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a new square

        Args:
            size (int): the size of the square

        """
        self.size = size
        self.position = position

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
            raise TypeError("size must be a integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property method to retrieve position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ class method that prints a square"""
        if (self.__size == 0):
            print("")
        else:
            [print("") for i in range(self.__position[1])]
            for x in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print("")
