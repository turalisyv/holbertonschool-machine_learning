#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


class NeuralNetwork:
    '''
    My class document
    '''
    def __init__(self, nx, nodes):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")

        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")

        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b1 = np.zeros(shape=(nodes, 1))
        self.__b2 = 0
        self.__A1 = 0
        self.__A2 = 0

    def sigmoid(self, x):
        '''My function document'''
        return 1 / (1 + np.exp(-x))

    def forward_prop(self, X):
        '''My functiion document'''
        self.__A1 = self.sigmoid(np.dot(self.__W1, X) + self.__b1)
        self.__A2 = self.sigmoid(np.dot(self.__W2, __A1) + self.__b2)
        return self.__A2

    @property
    def W1(self):
        return self.__W1

    @property
    def b1(self):
        return self.__b1

    @property
    def A1(self):
        return self.__A1

    @property
    def W2(self):
        return self.__W2

    @property
    def b2(self):
        return self.__b2

    @property
    def A2(self):
        return self.__A2
