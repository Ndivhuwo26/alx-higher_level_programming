#!/usr/bin/python3
'''the Module for Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''the subclass that represent a rectangle.'''
    def __init__(self, width, height):
        '''the Constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
