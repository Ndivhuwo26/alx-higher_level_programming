#!/usr/bin/python3

""" a Rectangle class."""


class Rectangle:
    """present a rectangle."""

    def __init__(self, width=0, height=0):
        """It initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """fetch/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """fetch/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """will Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """will Calculate the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """will Return a string representation of the rectangle."""
        return f"Rectangle(width={self.__width}, height={self.__height})"

    def __repr__(self):
        """will Return an official string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

