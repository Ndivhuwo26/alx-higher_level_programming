#!/usr/bin/python3
1-element_at.py

def element_at(my_list, idx):
    """this will retrive the element from list"""
     if idx < 0 or idx > len(my_list) - 1:
        return 'None'
    else:
        return my_list[idx]
