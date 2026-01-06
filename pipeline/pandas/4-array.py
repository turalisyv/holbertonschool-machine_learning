#!/usr/bin/env python3
'''
My module document
'''


def array(df):
    '''
    My function document
    '''
    return df[['High', 'Close']].tail(10).to_numpy()
