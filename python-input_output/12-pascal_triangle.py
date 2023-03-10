#!/usr/bin/python3
"""pascal traingle"""


def pascal_triangle(n):
    """traingle"""

    if n <= 0:
        return []
    pascal = []
    row = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(pascal[-1][j:j+2]))
        pascal.append(row)
    return pascal
