#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


def one_hot_encode(Y, classes):
    '''My function document'''
    res = np.zeros(shape=(len(Y), classes))

    for i in range(len(Y)):
        res[i][Y[i]] = 1

    return res