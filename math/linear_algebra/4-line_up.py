#!/usr/bin/env python3
'''
M module document
'''


def add_arrays(arr1, arr2):
    '''
    My function document
    '''
    if len(arr1) != len(arr2):
        return None

    arr3 = []
    for i in range(len(arr1)):
        arr3.append(arr1[i] + arr2[i])

    return arr3
