#!/usr/bin/python3

# 4-main.py

class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

# Test cases
try:
    my_square = Square(89)
    print("Area:", my_square.area())  # Output: 7921
    print("Size:", my_square.size)  # Output: 89
except Exception as e:
    print(e)

try:
    my_square.size = 3
    print("Area:", my_square.area())  # Output: 9
    print("Size:", my_square.size)  # Output: 3
except Exception as e:
    print(e)

try:
    my_square.size = "5 feet"
    print("Area:", my_square.area())
    print("Size:", my_square.size)
except Exception as e:
    print(e)

