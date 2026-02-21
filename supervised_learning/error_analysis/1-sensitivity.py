#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


def sensitivity(confusion):
    '''
    My function document
    '''
    confusion = np.array(confusion)

    TP = np.diag(confusion)
    FN = np.sum(confusion, axis=1) - TP

    sensitivity = TP / (TP + FN)

    return sensitivity
