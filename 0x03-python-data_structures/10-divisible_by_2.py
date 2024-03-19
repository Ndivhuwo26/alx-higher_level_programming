#!/usr/bin/python3
10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list and returns a list of Boolean values."""
    if len(my_list) == 0:
        return []

    return [num % 2 == 0 for num in my_list]

