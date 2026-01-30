#!/usr/bin/env python3
'''
My module document
'''


def mul_by_scalar(matrix, index, scalar):
    '''
    My function document
    '''
    n = len(matrix)

    for i in range(n):
        matrix[index][i] *= scalar

    return matrix


def to_upper_triangular(matrix):
    '''
    My function document
    '''
    n = len(matrix)

    for i in range(n):
        pivot = matrix[i][i]

        if pivot == 0:
            continue

        for j in range(i + 1, n):
            target_val = matrix[j][i]

            if target_val == 0:
                continue

            factor = target_val / pivot

            for k in range(i, len(matrix[0])):
                matrix[j][k] -= factor * matrix[i][k]

    return matrix


def determinant(matrix):
    '''
    My function document
    '''

    if matrix == [[]]:
        return 1

    if matrix == []:
        raise Exception("matrix must be a list of lists")

    for i in matrix:
        if not isinstance(i, list):
            raise Exception("matrix must be a list of lists")

    row = len(matrix)
    col = len(matrix[0])

    if row != col:
        raise Exception("matrix must be a square matrix")

    matrix = to_upper_triangular(matrix)
    det = 1
    for i in range(row):
        det = det * matrix[i][i]

    return int(det)
