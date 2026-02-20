#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


def create_confusion_matrix(labels, logits):
    '''
    My function document
    '''
    n = labels.shape[0]
    conf_mat = np.zeros((n, n), dtype=np.int32)
    row = np.where(labels == 1)[1]
    col = np.where(logits == 1)[1]

    for i, j in zip(row, col):
        conf_mat[i, j] = conf_mat[i, j] + 1

    np.set_printoptions(threshold=np.inf)
    return conf_mat
