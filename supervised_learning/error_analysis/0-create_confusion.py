#!/usr/bin/env python3
'''
My module document
'''


def create_confusion_matrix(labels, logits):
    '''
    My function document
    '''
    conf_mat = np.zeros((10, 10), dtype=np.int32)
    row = np.where(labels == 1)[1]
    col = np.where(logits == 1)[1]

    for i, j in zip(row, col):
        conf_mat[i, j] = conf_mat[i, j] + 1

    return conf_mat
