#!/usr/bin/env python3
'''
My module document
'''
import numpy as np
import matplotlib.pyplot as plt


def bars():
    '''
    My function documents
    '''
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4,3))
    plt.figure(figsize=(6.4, 4.8))
    bt = fruit[0]
    spc = ["Farrah", "Fred", "Felicia"]
    f = ["apples", "bananas", "oranges", "peaches"]
    plt.bar(spc, fruit[0], label=f[0], color="red", width=0.5)
    plt.bar(spc, fruit[1], bottom=bt, label=f[1], color="yellow", width=0.5)
    bt += fruit[1]
    plt.bar(spc, fruit[2], bottom=bt, label=f[2], color="#ff8000", width=0.5)
    bt += fruit[2]
    plt.bar(spc, fruit[3], bottom=bt, label=f[3], color="#ffe5b4", width=0.5)
    plt.yticks(np.arange(0, 81, 10))
    plt.ylabel("Quantity of Fruit")
    plt.title("Number of Fruit per Person")
    plt.legend()
