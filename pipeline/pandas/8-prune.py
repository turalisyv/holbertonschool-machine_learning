#!/usr/bin/env python3
'''
My module document
'''


def prune(df):
    '''
    My function document
    '''
    df = df.dropna(subset="Close")
    return df
