#!/usr/bin/env python3
'''
My module document
'''
import pandas as pd


def rename(df):
    '''
    My function document
    '''
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = df.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
