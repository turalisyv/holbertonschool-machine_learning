#!/usr/bin/env python3
"""My module document"""
import tensorflow.keras as K
import tensorflow as tf


def one_hot(labels, classes=None):
    """My function document"""
    return tf.one_hot(labels, classes)
