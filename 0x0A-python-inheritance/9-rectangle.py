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

    def area(self):
        '''a way  which returns area of rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''the String representation method.'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
