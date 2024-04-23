#!/usr/bin/python3
'''the Module for Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''the that subclass representing a rectangle.'''
    def __init__(self, size):
        '''the Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''the Method for area of square.'''
        return self.__size ** 2
