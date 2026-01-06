#!/usr/bin/env python3
'''
My module document
'''
import pandas as pd


def rename(df):
    '''
    My function document
    '''
    df.columns[0] = ["Datetime"]
    return df
