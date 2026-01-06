#!/usr/bin/env python3
'''
My module document
'''


def from_numpy(array):
    '''
    My function document
    '''
    col_list = [chr(ord('A') + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=col_list)
