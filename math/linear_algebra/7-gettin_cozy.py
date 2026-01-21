#!/usr/bin/env python3
'''
M module document
'''


def cat_matrices2D(mat1, mat2, axis=0):
    '''
    My function document
    '''
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    mat3 = []
    if axis == 0:
        mat3 = mat1 + mat2

    elif axis == 1:
        for i in range(len(mat1)):
            mat3.append(mat1[i] + mat2[i])

    return mat3
