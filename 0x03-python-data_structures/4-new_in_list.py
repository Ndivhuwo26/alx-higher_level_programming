#!/usr/bin/python3
4-new_in_list.py

    """Replaces an element in a list at a specific position without modifying the original list."""
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    new_list = list(my_list)
    new_list[idx] = element
    return new_list

