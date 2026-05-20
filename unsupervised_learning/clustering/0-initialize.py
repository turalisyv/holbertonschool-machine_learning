#!/usr/bin/env python3
"""My module document"""
import numpy as np


def initialize(X, k):
    """My function document"""
    try:
        if not isinstance(X, np.ndarray) or X.ndim != 2:
            return None

        if not isinstance(k, int) or k <= 0 or k > X.shape[0]:
            return None

        d = X.shape[1]

        low = np.min(X, axis=0)
        high = np.max(X, axis=0)

        centroids = np.random.uniform(
            low=low,
            high=high,
            size=(k, d)
        )

        return centroids
