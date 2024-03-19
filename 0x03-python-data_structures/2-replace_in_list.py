#!/usr/bin/python3
2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """Replace the element in a list at a certain position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list

