#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Simple square Matrix"""
    newMatrix = []
    for row in matrix:
        newRow = [x**2 for x in row]
        newMatrix.append(newRow)
    return newMatrix
