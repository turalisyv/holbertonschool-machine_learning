#!/usr/bin/env python3
'''
My module document
'''


def analyze(df):
    '''
    My function document
    '''
    df = df.set_index("Timestamp")
    return df.describe()
