#!/usr/bin/env python3
"""My module document"""
from sklearn.cluster import KMeans
import numpy as np

def initialize(X, k):
    """My function document"""
    model = KMeans(n_clusters=k)
    model.fit(X)

    return model.cluster_centers_
