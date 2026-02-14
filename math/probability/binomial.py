#!/usr/bin/env python3
'''
My module document
'''


class Binomial:
    '''
    My class document
    '''
    def __init__(self, data=None, n=1, p=0.5):

        if data is not None:

            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            var = sum((x - mean) ** 2 for x in data) / (len(data))

            p = 1 - (var / mean)
            n = round(mean / p)

            self.data = data
            self.n = n
            self.p = mean / n

        else:

            if n <= 0:
                raise ValueError("n must be a positive value")

            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")

            self.data = None
            self.n = n
            self.p = p

    @staticmethod
    def fact(n):
        '''
        factorial function
        '''
        if n < 0:
            return 0
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    def combination(self, n, k):
        '''
        combination function
        '''
        if k < 0 or k > n:
            return 0
        return self.fact(n) // (self.fact(k) * self.fact(n - k))

    def pdf(self, x):
        '''
        pdf function
        '''
        x = int(x)

        if x < 0 or x > self.n:
            return 0

        return (
            self.combination(self.n, x)
            * (self.p ** x)
            * ((1 - self.p) ** (self.n - x))
        )

    def cdf(self, x):
        '''
        cdf function
        '''
        x = int(x)

        if x < 0:
            return 0

        if x >= self.n:
            return 1

        total = 0
        for k in range(0, x + 1):
            total += self.pdf(k)

        return total
