#!/usr/bin/python3
'''this a Module for is_kind_of_class method.'''

def is_kind_of_class(obj, a_class):
    ''' Checks if an object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class.'''
    return isinstance(obj, a_class)
