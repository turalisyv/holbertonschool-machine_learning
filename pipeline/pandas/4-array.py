#!/usr/bin/env python3
'''
My module document
'''


def array(df):
    return df[['High', 'Close']].tail(10).to_numpy()
