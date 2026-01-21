#!/usr/bin/env python3
'''
My module document
'''


def matrix_shape(matrix):
    '''
    My function document
    '''
    shape = []
    while True:
        shape.append(len(matrix))
        matrix = matrix[0]

        if isinstance(matrix, int):
            break

    return shape
