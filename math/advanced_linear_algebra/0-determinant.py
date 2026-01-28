#!/usr/bin/env python3
'''
My module document
'''


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

        if len(i) != len(matrix):
            raise Exception("matrix must be a square matrix")

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1] 

    if len(matrix) == 3:
        a1 = matrix[0][0] * matrix[1][1] * matrix[2][2]
        a2 = matrix[1][0] * matrix[2][1] * matrix[0][2]
        a3 = matrix[2][0] * matrix[0][1] * matrix[1][2]

        a4 = matrix[0][2] * matrix[1][1] * matrix[2][0]
        a5 = matrix[1][2] * matrix[2][1] * matrix[0][0]
        a6 = matrix[2][2] * matrix[0][1] * matrix[1][0]

        return ((a1 + a2 + a3) - (a4 + a5 + a6))
