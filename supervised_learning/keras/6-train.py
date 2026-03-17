#!/usr/bin/env python3
"""My module document"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size,
                epochs, verbose=True, shuffle=False,
                validation_data=None, early_stopping=False,
                patience=0):
    """My function document"""

    if early_stopping is True:
        es = K.callbacks.EarlyStopping(monitor='val_loss', patience=patience)
        history = network.fit(
            x=data,
            y=labels,
            batch_size=batch_size,
            validation_data=validation_data,
            epochs=epochs,
            verbose=verbose,
            shuffle=shuffle,
            callbacks=[es]
        )

        return history

    history = network.fit(
        x=data,
        y=labels,
        batch_size=batch_size,
        validation_data=validation_data,
        epochs=epochs,
        verbose=verbose,
        shuffle=shuffle
    )

    return history
