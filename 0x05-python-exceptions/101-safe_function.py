#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
    else:
        return res

if __name__ == "__main__":
    def example_function(x, y):
        return x / y

    x = 10
    y = 0
    result = safe_function(example_function, x, y)
    print("Result:", result)

