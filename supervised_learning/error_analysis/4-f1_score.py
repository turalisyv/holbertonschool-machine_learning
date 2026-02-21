#!/usr/bin/env python3
'''
My module document
'''
import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    '''
    My function document
    '''
    confusion = np.array(confusion)

    TP = np.diag(confusion)
    FP = np.sum(confusion, axis=0) - TP
    FN = np.sum(confusion, axis=1) - TP

    precision = precision(confusion)
    sensitivity = sensitivity(confusion)

    f1 = 2 * precision * sensitivity / (precision + sensitivity)

    return f1
