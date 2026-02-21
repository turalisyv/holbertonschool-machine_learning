#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


def precision(confusion):
    '''
    My function document
    '''
    confusion = np.array(confusion)

    TP = np.diag(confusion)
    FP = np.sum(confusion, axis=0) - TP

    precision = TP / (TP + FP)

    return precision
