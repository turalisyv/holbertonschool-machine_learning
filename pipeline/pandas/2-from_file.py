#!/usr/bin/env python3
'''
My module document
'''
import pandas as pd


def from_file(filename, delimiter):
    '''
    My function document
    '''
    return pd.read_csv(filename, sep=delimiter)
