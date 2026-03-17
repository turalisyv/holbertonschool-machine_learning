#!/usr/bin/env python3
"""My module document"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size,
                epochs, verbose=True, shuffle=False):
    """My function document"""
    history = network.fit(
        x=data,
        y=labels,
        batch_size=batch_size,
        validation_data=validation_data,
        epochs=epochs,
        verbose=verbose,
        shuffle=shuffle,
    )

    return history
