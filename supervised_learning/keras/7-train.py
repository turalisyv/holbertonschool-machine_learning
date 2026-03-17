#!/usr/bin/env python3
"""My module document"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size,
                epochs, verbose=True, shuffle=False,
                validation_data=None, early_stopping=False,
                patience=0, learning_rate_decay=False,
                alpha=0.1, decay_rate=1,):
    """My function document"""

    dcy = K.optimizers.schedules.InverseTimeDecay(
        initial_learning_rate=alpha,
        decay_rate=decay_rate,
    )

    es = K.callbacks.EarlyStopping(monitor='val_loss', patience=patience)

    history = network.fit(
        x=data,
        y=labels,
        batch_size=batch_size,
        validation_data=validation_data,
        epochs=epochs,
        verbose=verbose,
        shuffle=shuffle,
        callbacks=[es] if early_stopping else None,
        learning_rate=dcy if learning_rate_decay else None
    )

    return history
