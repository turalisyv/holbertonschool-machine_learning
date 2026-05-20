#!/usr/bin/env python3
"""My module document"""
import numpy as np


def initialize(X, k):
    """My function document"""
    try:
        d = X.ndim
        centroids = np.random.uniform(low=np.min(X, axis=0), high=np.max(X, axis=0), size=(k, d))

        return centroids

    except ValueError:
        return None
