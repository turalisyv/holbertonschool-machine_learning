#!/usr/bin/env python3
'''
My module document
'''


def poly_derivative(poly):
    '''
    My function document
    '''

    if not isinstance(poly, list):
        return None

    for i in poly:
        if not isinstance(i, (int, float)):
            return None


    der = []

    if poly == [0] or poly == [] or len(poly) == 1:
        return [0]

    for i in range(1, len(poly)):
        der.append(i * poly[i])

    return der
