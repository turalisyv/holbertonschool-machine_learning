#!/usr/bin/env python3
'''
My module document
'''
import pandas as pd


dc = {"First": [0.0, 0.5, 1.0, 1.5], "Second": ["one", "two", "three", "four"]}
df = pd.DataFrame.from_dict(dc, orient='columns')
df.index = ['A', 'B', 'C', 'D']
