def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if m_a == [] or any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if m_b == [] or any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if any(not all(isinstance(ele, (int, float)) for ele in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if any(not all(isinstance(ele, (int, float)) for ele in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = [[m_b[j][i] for j in range(len(m_b))] for i in range(len(m_b[0]))]

    new_matrix = [[sum(a * b for a, b in zip(row, col)) for col in inverted_b] for row in m_a]

    return new_matrix

