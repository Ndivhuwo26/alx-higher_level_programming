#!/usr/bin/python3
6-print_matrix_integer.py

def print_matrix_integer(matrix=None):
    """Prints a matrix of integers."""
    if matrix is None:
        matrix = []

    for row in matrix:
        print(" ".join("{:d}".format(col) for col in row))

