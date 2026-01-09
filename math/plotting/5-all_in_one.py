#!/usr/bin/env python3
'''
My module document
'''
import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    '''
    My function document
    '''
    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    fig = plt.figure(figsize=(6, 6))
    gs = fig.add_gridspec(3, 2)

    ax1 = fig.add_subplot(gs[0, 0])
    x0 = np.arange(0, 11)
    plt.xlim(0, 10)
    plt.plot(x0, y0, c="red")

    ax2 = fig.add_subplot(gs[0, 1])
    plt.title("Men's Height vs Weight")
    plt.xlabel("Height (in)")
    plt.ylabel("Weight (lbs)")
    plt.scatter(x1, y1, c='magenta')

    ax3 = fig.add_subplot(gs[1, 0])
    plt.title("Exponential Decay of C-14")
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.yscale('log')
    plt.xlim(0, 28650)
    plt.plot(x2, y2)

    ax4 = fig.add_subplot(gs[1, 1])
    plt.title("Exponential Decay of Radioactive Elements")
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")

    plt.xlim(0, 20000)
    plt.ylim(0, 1)

    plt.plot(x3, y31, c="red", linestyle="--", label="C-14")
    plt.plot(x3, y32, c="green", label="Ra-226")
    plt.legend()

    ax5 = fig.add_subplot(gs[2, :])
    plt.title("Project A")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    plt.xticks(np.arange(0, 101, step=10))
    plt.hist(student_grades, range=(0, 100), edgecolor='black')

    plt.show()
