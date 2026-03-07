#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


class DeepNeuralNetwork:
    '''
    My class document
    '''
    def __init__(self, nx, layers):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for i in range(self.L):
            if not isinstance(layers[i], int) or layers[i] < 1:
                raise TypeError("layers must be a list of positive integers")

            if i == 0:
                self.weights['W1'] = np.random.randn(
                    layers[i], nx) * np.sqrt(2 / nx)
            else:
                self.weights[f'W{i + 1}'] = np.random.randn(
                    layers[i], layers[i - 1]) * np.sqrt(2 / layers[i - 1])

            self.weights[f'b{i + 1}'] = np.zeros((layers[i], 1))

    def sigmoid(self, x):
        '''My function document'''
        return 1 / (1 + np.exp(-x))

    def forward_prop(self, X):
        '''My function document'''
        self.__cache['A0'] = X
        for i in range(1, self.__L + 1):
            W = self.__weights['W' + str(i)]
            b = self.__weights['b' + str(i)]
            A_prev = self.__cache['A' + str(i - 1)]
            Z = np.dot(W, A_prev) + b
            A = self.sigmoid(Z)
            self.__cache['A' + str(i)] = A
        return self.__cache['A' + str(self.__L)], self.__cache

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
        A, _ = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        '''My function document'''
        m = Y.shape[1]
        dz = cache['A' + str(self.__L)] - Y

        for i in range(self.__L, 0, -1):
            A_prev = cache['A' + str(i - 1)]
            W_curr = self.__weights['W' + str(i)]
            b_curr = self.__weights['b' + str(i)]

            dw = (1 / m) * np.dot(dz, A_prev.T)
            db = (1 / m) * np.sum(dz, axis=1, keepdims=True)

            if i > 1:
                dz = np.dot(W_curr.T, dz) * (A_prev * (1 - A_prev))

            self.__weights['W' + str(i)] = W_curr - alpha * dw
            self.__weights['b' + str(i)] = b_curr - alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        '''My function document'''
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        for iter in range(iterations):
            A, cache = self.forward_prop(X)
            self.gradient_descent(Y, cache, alpha)

        return self.evaluate(X, Y)

    @property
    def L(self):
        return self.__L

    @property
    def cache(self):
        return self.__cache

    @property
    def weights(self):
        return self.__weights
