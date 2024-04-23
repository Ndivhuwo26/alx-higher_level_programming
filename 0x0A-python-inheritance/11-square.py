#!/usr/bin/python3
'''the Module for Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''the  subclass that  represent a rectangle.'''
    def __init__(self, size):
        '''the Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''the Method for area of square.'''
        return self.__size ** 2

    def __str__(self):
        '''this will return a string representation of this square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
