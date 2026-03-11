#!/usr/bin/env python3
"""My module document"""
import tensorflow.keras as K

    
def optimize_model(network, alpha, beta1, beta2):
    """My function document"""
    opt = K.optimizers.Adam(learning_rate=alpha, beta_1=beta1, beta_2=beta2)
    loss_fn = "categorical_crossentropy"

    network.compile(optimizer=opt, loss=loss_fn, metrics=["accuracy"])
