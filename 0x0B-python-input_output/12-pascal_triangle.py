#!/usr/bin/python3
"""Main"""


def pascal_triangle(n):
    """Doc"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for index in range(len(tri) - 1):
            tmp.append(tri[index] + tri[index + 1])
        tmp.append(1)
        triangles.append(tmp)

    return triangles
