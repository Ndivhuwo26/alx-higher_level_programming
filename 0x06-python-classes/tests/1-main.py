#!/usr/bin/python3

# 1-main.py

class Square:
    def __init__(self, size):
        self.__size = size

my_square = Square(3)
print(type(my_square))  # Output: <class '__main__.Square'>
print(my_square.__dict__)  # Output: {'_Square__size': 3}

# Accessing private attribute directly raises AttributeError
try:
    print(my_square.size)  # Output: AttributeError: 'Square' object has no attribute 'size'
except AttributeError as e:
    print(e)

# Accessing mangled private attribute also raises AttributeError
try:
    print(my_square.__size)  # Output: AttributeError: 'Square' object has no attribute '__size'
except AttributeError as e:
    print(e)

