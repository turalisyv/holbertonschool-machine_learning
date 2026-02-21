#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


def specificity(confusion):
    '''
    My function document
    '''
    confusion = np.array(confusion)

    TP = np.diag(confusion)
    FN = np.sum(confusion, axis=1) - TP
    FP = np.sum(confusion, axis=0) - TP
    TN = np.sum(confusion) - (TP + FN + FP)

    specificity = TN / (TN + FP)

    return specificity
