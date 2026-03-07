#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


def one_hot_encode(Y, classes):
    """
    My function document
    """
    try:
        
        if not isinstance(Y, np.ndarray):
            return None
        
        m = Y.shape[0]
        one_hot = np.zeros((classes, m))
        one_hot[Y, np.arange(m)] = 
        return one_hot
        
    except Exception:
        return None
