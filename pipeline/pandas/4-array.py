#!/usr/bin/env python3
'''
My module document
'''
import pandas as pd
import numpy as np


def array(df):
    return np.array(df[["High", "Close"]].tail(10))
