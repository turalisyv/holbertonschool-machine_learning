#!/usr/bin/env python3
"""My module document"""
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """My function document"""
    return K.ops.one_hot(labels, 10)
