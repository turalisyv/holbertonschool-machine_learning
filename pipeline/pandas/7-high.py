#!/usr/bin/env python3
'''
My module document
'''


def high(df):
    '''
    My function document
    '''
    df = df.dropna()
    return df.sort_values("High")[::-1].head()
