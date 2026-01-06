#!/usr/bin/env python3
'''
My module document
'''


def fill(df):
    '''
    My function document
    '''
    df = df.drop(columns=["Weighted_Price"])
    df['Close'] = df['Close'].ffill()
    df['High'], df['Low'], df['Open'] = df['Close'], df['Close'], df['Close']
    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)
    return df
