#!/usr/bin/env python3
"""My module document"""
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """My function document"""
    if classes is None:
        classes = len(set(labels))
    return K.ops.one_hot(labels, classes)
