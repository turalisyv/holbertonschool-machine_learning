#!/usr/bin/env python3
'''
My module document
'''


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

    res = np.zeros_like(P)
    for i in range(len(P)):
        res[i] = comb(n, x) * P[i] ** x * (1 - P[i]) ** (n - x)

    return res
