#!/usr/bin/python3
3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Prints the reversed list of integers."""
    reversed_list = my_list[::-1]
    for num in reversed_list:
        print(f"{num}")


