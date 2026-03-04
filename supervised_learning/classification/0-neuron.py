#!/usr/bin/env python3
'''
My module document
'''
import numpy as np


class Neuron:
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        
        if nx < 1:
            raise ValueError("nx must be a positive integer")