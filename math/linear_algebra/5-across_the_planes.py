#!/usr/bin/env python3
'''
M module document
'''


def add_matrices2D(mat1, mat2):
    '''
    My function document
    '''
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    mat3 = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        mat3.append(row)

    return mat3
