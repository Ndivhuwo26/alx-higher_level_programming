#!/usr/bin/python3

# 3-main.py

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

# Test cases
try:
    my_square_1 = Square(3)
    print("Area:", my_square_1.area())  # Output: 9
except Exception as e:
    print(e)

try:
    print(my_square_1.size)  # Output: AttributeError: 'Square' object has no attribute 'size'
except AttributeError as e:
    print(e)

try:
    print(my_square_1.__size)  # Output: AttributeError: 'Square' object has no attribute '__size'
except AttributeError as e:
    print(e)

try:
    my_square_2 = Square(5)
    print("Area:", my_square_2.area())  # Output: 25
except Exception as e:
    print(e)

