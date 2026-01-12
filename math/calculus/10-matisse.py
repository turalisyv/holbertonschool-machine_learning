#!/usr/bin/env python3
'''
My module document
'''


def poly_derivative(poly):
    '''
    My function document
    '''
    der = []

    if poly == [0] or poly == []:
        return poly

    for i in range(1, len(poly)):
        der.append(i * poly[i])

    return der
