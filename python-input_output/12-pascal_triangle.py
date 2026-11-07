#!/usr/bin/python3
"""Module 12-pascal_triangle: builds Pascal's triangle as nested lists."""


def pascal_triangle(n):
    """Return a list of lists of integers for Pascal's triangle of size n.

    Args:
        n (int): the number of rows; an empty list is returned if n <= 0.
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
