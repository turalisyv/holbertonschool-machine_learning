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
    
    @property
    def get_W(self):
        return self.__W

    @property
    def get_b(self):
        return self.__b

    @property
    def get_A(self):
        return self.__A
