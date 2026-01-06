#!/usr/bin/env python3
'''
My module document
'''


def array(df):
    return [[i, j] for i, j in zip(list(df["High"][-10:]), list(df["Close"][-10:]))]
