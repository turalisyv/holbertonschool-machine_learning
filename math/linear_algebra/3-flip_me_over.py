#!/usr/bin/env python3
'''
M module document
'''

def matrix_transpose(matrix):
    '''
    My function document
    '''
    transpose = []

    for i in range(len(matrix[0])):
        col = []
        for j in range(len(matrix)):
            col.append(matrix[j][i])
        transpose.append(col)

    return transpose
