#!/usr/bin/python3
9-max_integer.py


 """Finds the biggest integer of a list."""
def max_integer(my_list=[]):
    new_list = []
    if my_list:
        my_list.sort(reverse=True)
        return (my_list[0])
    return (None)
    
