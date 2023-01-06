#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lst = []
    for row in matrix:
        lst.append(list(map(lambda x: x*x, row)))
    return lst
