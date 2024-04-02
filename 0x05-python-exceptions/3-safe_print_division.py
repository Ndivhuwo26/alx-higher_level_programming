#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div

if __name__ == "__main__":
    a = 10
    b = 2
    division_result = safe_print_division(a, b)
    print("Division result:", division_result)

