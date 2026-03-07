#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


class Neuron:
    '''
    My class document
    '''
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")

        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    def sigmoid(self, x):
        '''My function document'''
        return 1 / (1 + np.exp(-x))

    def forward_prop(self, X):
        '''My functiion document'''
        self.__A = self.sigmoid(np.dot(self.__W, X) + self.__b)
        return self.__A

    def cost(self, Y, A):
        '''My function document'''
        m = Y.shape[1]
        C = - (1 / m) * np.sum(
            np.multiply(
                Y, np.log(A)) + np.multiply(
                1 - Y, np.log(1.0000001 - A)))
        return C

    def evaluate(self, X, Y):
        '''My function document'''
        y_pred = self.forward_prop(X)
        A = self.cost(Y, y_pred)
        return y_pred, A

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A
