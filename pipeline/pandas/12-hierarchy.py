#!/usr/bin/env python3
'''
My module document
'''
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    '''
    My function document
    '''
    df1 = df1.set_index('Timestamp')
    df2 = df2.set_index('Timestamp')
    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]
    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    df = df.swaplevel(0, 1).sort_index()
    return df
