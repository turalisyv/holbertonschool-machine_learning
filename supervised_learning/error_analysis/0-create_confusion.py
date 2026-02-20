#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


def create_confusion_matrix(labels, logits):
    '''
    My function document
    '''
    return np.dot(labels.T, logits)
