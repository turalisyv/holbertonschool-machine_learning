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
        y_pred = np.int32(y_pred > 0.5)
        return y_pred, A

    def gradient_descent(self, X, Y, A, alpha=0.05):
        '''My function document'''
        m = Y.shape[1]

        dZ = A - Y
        dW = (1 / m) * np.dot(dZ, X.T)
        db = (1 / m) * np.sum(dZ)

        self.__W = self.__W - alpha * dW
        self.__b = self.__b - alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        '''My function document'''
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")

        if iterations < 0:
            raise ValueError("iterations must be a positive integer")

        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")

        if alpha < 0:
            raise ValueError("alpha must be positive")

        steps = [i for i in range(0, iterations + 1, step)]
        costs = []

        for iter in range(iterations + 1):
            self.forward_prop(X)
            self.gradient_descent(X, Y, self.A, alpha=alpha)

            if iter % step == 0:
                cost = self.cost(Y, self.A)
                costs.append(cost)
                if verbose:
                    print("Cost after {} iterations: {}".format(iter, cost))

        if graph:
            plt.plot(steps, costs)
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.title("Training Cost")
            plt.show()

        return self.evaluate(X, Y)

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A
