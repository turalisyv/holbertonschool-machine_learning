#!/usr/bin/env python3
"""My module document"""
import tensorflow as tf


def build_model(nx, layers, activations, lambtha, keep_prob):
    """My function document"""
    model = [tf.keras.layers.Input(shape=(nx,))]

    for n, act in zip(layers, activations):
        model.append(tf.keras.layers.Dense(
            units=n,
            activation=act, 
            kernel_regularizer=tf.keras.regularizers.l2(lambtha)))
        
        model.append(tf.keras.layers.Dropout(rate=keep_prob))

    model.pop()

    return tf.keras.Sequential(model)
