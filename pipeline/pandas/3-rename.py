#!/usr/bin/env python3
'''
My module document
'''
import pandas as pd


def rename(df):
    '''
    My function document
    '''
    df.rename({"Timestamp": "Datetime"})
    return df
