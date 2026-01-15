#!/usr/bin/env python3
'''
My module document
'''


def poly_integral(poly, C=0):
    '''
    My function document
    '''

    if not isinstance(poly, list) or poly == []:
        return None

    for i in poly:
        if not isinstance(i, (int, float)):
            return None

    if not isinstance(C, (int, float)):
        return None

    integral = [C]

    for i in range(0, len(poly)):
        integral.append(poly[i] * (1 / (i + 1)))

    return integral
