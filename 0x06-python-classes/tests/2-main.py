#!/usr/bin/python3

# 2-main.py

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

# Test cases
try:
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__) 
except Exception as e:
    print(e)

try:
    my_square_2 = Square()
    print(type(my_square_2))  
    print(my_square_2.__dict__) 
except Exception as e:
    print(e)

try:
    print(my_square_1.size)
except AttributeError as e:
    print(e)

try:
    print(my_square_1.__size)
except AttributeError as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
except Exception as e:
    print(e)

