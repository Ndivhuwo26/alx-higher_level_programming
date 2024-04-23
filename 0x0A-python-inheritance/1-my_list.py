#!/usr/bin/python3
'''this a Module for MyList class.'''

class MyList(list):
    ''' MyList class.'''
    def print_sorted(self):
        '''Method for writting a sorted list.'''
        print(sorted(self))
