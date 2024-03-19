#!/usr/bin/python3
11-delete_at.py

def delete_at(my_list=None, idx=0):
    """Deletes the item at a specific position in a list."""
    if my_list is None:
        my_list = []

    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        del my_list[idx]
        return my_list

