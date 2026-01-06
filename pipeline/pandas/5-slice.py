#!/usr/bin/env python3
'''
My module document
'''


def slice(df):
    '''
    My function document
    '''
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].loc[::60]
