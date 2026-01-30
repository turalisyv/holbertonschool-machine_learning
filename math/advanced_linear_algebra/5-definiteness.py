#!/bin/bash/env python3
'''
My module document
'''
import numpy as np


def definiteness(matrix):
    '''
    My function document
    '''

    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    try:
        np.linalg.eigvals(matrix)
    except Exception as e:
        return None

    A = np.linalg.eigvals(matrix)

    if np.all(A > 0):
        return "Positive definite"

    elif np.all(A < 0):
        return "Negative definite"

    elif np.all(A >= 0):
        return "Positive semi-definite"

    elif np.all(A <= 0):
        return "Negative semi-definite"

    else:
        return "Indefinite"
