#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception:", e, file=sys.stderr)
        return False

if __name__ == "__main__":
    value = "abc"
    success = safe_print_integer_err(value)
    print("Success:", success)

