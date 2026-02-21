#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


def f1(confusion):
    '''
    My function document
    '''
    confusion = np.array(confusion)

    TP = np.diag(confusion)
    FP = np.sum(confusion, axis=0) - TP
    FN = np.sum(confusion, axis=1) - TP

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)

    f1 = 2 * precision * recall / (precision + recall)

    return f1
