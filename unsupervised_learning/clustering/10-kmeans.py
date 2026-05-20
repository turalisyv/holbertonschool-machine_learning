#!/usr/bin/env python3
"""My module document"""
import sklearn.cluster

def kmeans(X, k):
    """My function document"""
    model = sklearn.cluster.KMeans(n_clusters=k)
    model.fit(X)

    return model.cluster_centers_, model.predict(X)
