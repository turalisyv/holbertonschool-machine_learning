#!/usr/bin/env python3
"""My module document"""
import sklearn.mixture

def gmm(X, k):
    """My function document"""
    model = sklearn.mixture.GaussianMixture(k)
    model.fit(X)

    return (
        model.weights_,
        model.means_,
        model.covariances_,
        model.predict(X),
        model.bic(X)
    )
