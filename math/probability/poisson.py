#!/usr/bin/env python3
'''
My module document
'''


class Poisson:
    '''
    My class document
    '''
    def __init__(self, data=None, lambtha=1.):
        self.e = 2.7182818285
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

    @staticmethod
    def fact(n):
        '''
        factorial function
        '''
        res = 1
        for i in range(1, n+1):
            res = res * i

        return res

    def pmf(self, k):
        '''
        pmf function
        '''
        k = int(k)
        if k < 0:
            return 0

        return (self.e**(-self.lambtha) * self.lambtha**(k)) / Poisson.fact(k)

    def cdf(self, k):
        '''
        cdf function
        '''
        k = int(k)
        if k < 0:
            return 0

        res = 0
        for i in range(k+1):
            res = res + self.pmf(i)

        return res
