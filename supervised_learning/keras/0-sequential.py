#!/usr/bin/env python3
"""My module document"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """My function document"""
    model = [K.layers.Input(shape=(nx,))]

    for n, act in zip(layers, activations):
        model.append(K.layers.Dense(
            units=n,
            activation=act, 
            kernel_regularizer=K.regularizers.l2(lambtha)))
        
        model.append(K.layers.Dropout(rate=keep_prob))

    model.pop()

    return K.Sequential(model)
