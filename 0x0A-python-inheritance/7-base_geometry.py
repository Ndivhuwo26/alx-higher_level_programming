#!/usr/bin/python3
'''the Module for BaseGeometry class.'''


class BaseGeometry:
    '''the  BaseGeometry class.'''
    def area(self):
        '''this is a way to compute this area.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''this is a way  for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
