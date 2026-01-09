#!/usr/bin/env python3
'''
My module document
'''
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    '''
    My function document
    '''
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.hist(student_grades, range=(0, 100), edgecolor='black')
    plt.show()
