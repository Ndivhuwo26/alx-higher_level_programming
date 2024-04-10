#!/usr/bin/python3

"""It define a class Square."""


class Square:
    """It represent a square."""

    def __init__(self, size=0):
        """It will initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Will return the current area of the square."""
        return (self.__size * self.__size)

