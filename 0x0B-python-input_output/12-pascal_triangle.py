#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)

    return triangle

