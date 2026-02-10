#!/usr/bin/env python3
'''
My module document
'''


class Normal:
    '''
    My class document
    '''
    def __init__(self, data=None, mean=0., stddev=1.):
        self.e = 2.7182818285
        self.data = data
        self.mean = mean

        if stddev > 0:
            self.stddev = stddev
        else:
            raise ValueError("stddev must be a positive value")

        if self.data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = sum(self.data) / len(self.data)

            self.variance = 0
            for i in self.data:
                self.variance += (i - self.mean) ** 2

            self.stddev = self.sqrt(self.variance / len(self.data))

    def z_score(self, x):
        '''
        My z_score function
        '''
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        '''
        My x_value function
        '''
        return z * self.stddev + self.mean

    @staticmethod
    def sqrt(x):
        '''
        My sqrt function
        '''
        res = x

        for i in range(1000):
            res = 0.5 * (res + x / res)

        return res
