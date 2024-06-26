#!/usr/bin/python3

"""this defines a class Square."""


class Square:
    """this represents a square."""

    def __init__(self, size=0):
        """it Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """this Returns the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """it Defines the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """this Defines the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """this Defines the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """it Defines the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """it Defines the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """this Defines the >= compmarison to a Square."""
        return self.area() >= other.area()

