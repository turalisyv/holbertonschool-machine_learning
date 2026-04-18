#!/usr/bin/env python3
'''My module document'''

from tensorflow import keras as K


def identity_block(A_prev, filters):
    '''My class document'''
    F11, F3, F12 = filters

    X_shortcut = A_prev

    initializer = K.initializers.he_normal(seed=0)

    X = K.layers.Conv2D(filters=F11, kernel_size=(1, 1), strides=(1, 1),
                        padding='valid', kernel_initializer=initializer)(A_prev)
    X = K.layers.BatchNormalization(axis=-1)(X)
    X = K.layers.Activation('relu')(X)

    X = K.layers.Conv2D(filters=F3, kernel_size=(3, 3), strides=(1, 1),
                        padding='same', kernel_initializer=initializer)(X)
    X = K.layers.BatchNormalization(axis=-1)(X)
    X = K.layers.Activation('relu')(X)

    X = K.layers.Conv2D(filters=F12, kernel_size=(1, 1), strides=(1, 1),
                        padding='valid', kernel_initializer=initializer)(X)
    X = K.layers.BatchNormalization(axis=-1)(X)

    X = K.layers.Add()([X, X_shortcut])

    X = K.layers.Activation('relu')(X)

    return X
