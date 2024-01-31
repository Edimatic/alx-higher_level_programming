#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists.
        ValueError: If m_a or m_b is empty or if matrices can't be multiplied.
        TypeError: If an element in m_a or m_b is not an integer or float.
        TypeError: If m_a or m_b is not a rectangle.

    Returns:
        A new matrix representing the result of the multiplication.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if m_a == [] or any(len(row) == 0 for row in m_a) or m_b == [] or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

