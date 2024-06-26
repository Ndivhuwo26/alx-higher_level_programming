#!/usr/bin/python3
'''this a Module for inherits_from method.'''

def inherits_from(obj, a_class):
    '''Checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class.
'''
    return isinstance(obj, a_class) and type(obj) != a_class
