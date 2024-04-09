#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Parameters:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The divisor.

    Returns:
    list of lists: The new matrix with elements divided by div and rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats, or if div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            result = round(num / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix

