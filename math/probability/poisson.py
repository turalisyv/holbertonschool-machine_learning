#!/usr/bin/env python3
'''
My module document
'''


class Poisson:
    '''
    My class document
    '''
    def __init__(self, data=None, lambtha=1.):
        self.data = data

        if lambtha > 0:
            self.lambtha = lambtha
        else:
            raise ValueError("lambtha must be a positive value")

        if self.data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = sum(self.data) / len(self.data)
