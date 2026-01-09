#!/usr/bin/env python3
'''
My module document
'''
import numpy as np
import matplotlib.pyplot as plt


def bars():
    '''
    My function document
    '''
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4,3))
    plt.figure(figsize=(6.4, 4.8))

    spc = ["Farrah", "Fred", "Felicia"]
    plt.bar(spc, fruit[0], label="apples", color="red", width=0.5)
    plt.bar(spc, fruit[1], bottom=fruit[0], label="bananas", color="yellow", width=0.5)
    plt.bar(spc, fruit[2], bottom=fruit[0]+fruit[1], label="oranges", color="#ff8000", width=0.5)
    plt.bar(spc, fruit[3], bottom=fruit[0]+fruit[1]+fruit[2], label="peaches", color="#ffe5b4", width=0.5)
    plt.yticks(np.arange(0, 81, 10))
    plt.ylabel("Quantity of Fruit")
    plt.title("Number of Fruit per Person")
    plt.legend()
