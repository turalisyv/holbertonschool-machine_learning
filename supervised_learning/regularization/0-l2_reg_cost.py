#!/usr/bin/env python3
"""Cost of a neural network with L2 regularization"""
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """Cost of a neural network with L2 regularization"""
    frobenius_sum = sum(
        np.sum(np.square(weights[f'W{layer}']))
        for layer in range(1, L + 1)
    )

    # L2 regularization term
    l2_term = (lambtha / (2 * m)) * frobenius_sum
    return cost + l2_term
