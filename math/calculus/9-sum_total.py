#!/usr/bin/env python3
'''
My module document
'''


def summation_i_squared(n):
    '''
    My function document
    '''
    try:
        return sum(map(lambda i: i**2, range(0, n+1)))

    except TypeError:
        return None
