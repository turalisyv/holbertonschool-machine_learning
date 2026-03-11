#!/usr/bin/env python3
"""My module document"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """My function document"""
    input = K.layers.Input(shape=(nx,))
    output = input
    for i, (n, act) in enumerate(zip(layers, activations)):
        output = K.layers.Dense(
            units=n,
            activation=act,
            kernel_regularizer=K.regularizers.l2(lambtha)
        )(output)

        if i < len(layers) - 1:
            output = K.layers.Dropout(rate=1.0 - keep_prob)(output)

    model = K.models.Model(input, output)

    return model
