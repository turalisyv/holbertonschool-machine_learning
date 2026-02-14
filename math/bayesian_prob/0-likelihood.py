#!/usr/bin/env python3
'''
My module document
'''
import numpy


def fact(n):
        '''
        factorial function
        '''
        if n < 0:
            return 0
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

def comb(n, k):
    '''
    comb function
    '''
    if k < 0 or k > n:
        return 0
    return fact(n) // (fact(k) * fact(n - k))

def likelihood(x, n, P):
    '''
    My function document
    '''

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
            )
    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, numpy.ndarray):
        raise TypeError("P must be a 1D numpy.ndarray")

    res = np.zeros_like(P)
    for i in range(len(P)):
        if P[i] > 1 or P[i] < 0:
            raise ValueError("All values in P must be in the range [0, 1]")
        res[i] = comb(n, x) * P[i] ** x * (1 - P[i]) ** (n - x)

    return res
