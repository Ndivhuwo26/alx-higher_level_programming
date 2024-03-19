#!/usr/bin/python3
5-no_c.py

    """Removes all occurrences of the characters 'c' and 'C' from a string."""
    def no_c(my_string):
    new_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_string += elements
    return new_string

