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

            for i in self.data:
                self.stddev += (i - self.mean) ** 2

            self.stddev = self.sqrt(self.stddev /  len(self.data))

    @staticmethod
    def sqrt(x):
        res = x

        for i in range(1000000):
            res = 0.5 * (res + x / res)

        return res
