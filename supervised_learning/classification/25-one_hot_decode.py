#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


def one_hot_decode(one_hot):
    '''My function document'''
    if type(one_hot) is not np.ndarray or len(one_hot.shape) != 2:
        return None

    res = one_hot.transpose().argmax(axis=1)
    return res
