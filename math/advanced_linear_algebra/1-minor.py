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

    if matrix == []:
        raise Exception("matrix must be a list of lists")

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a list of lists")

    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            raise ValueError("matrix must be a square matrix")

    row = len(matrix)
    col = len(matrix[0])

    matrix = to_upper_triangular(matrix)
    det = 1
    for i in range(row):
        det = det * matrix[i][i]

    return int(det)

def remove_row_col(matrix, row, col):
    res = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix)):
            if i != row and j != col:
                temp.append(matrix[i][j])

        res.append(temp)

    del res[row]
    return res


def minor(matrix):
    """
    My function document
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 1:
        return [[1]]

    # Initialize a new matrix of the same size with zeros
    res_matrix = [[0 for _ in range(n)] for _ in range(n)]


    if matrix == [[]]:
        return 1

    if matrix == []:
        raise Exception("matrix must be a list of lists")

    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            raise ValueError("matrix must be a non-empty square matrix")


    for i in range(n):
        for j in range(n):
            sub = remove_row_col(matrix, i, j)
            res_matrix[i][j] = determinant(sub)

    return res_matrix
