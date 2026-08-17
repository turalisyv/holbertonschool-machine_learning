#!/usr/bin/env python3
""" An early stopping"""


def early_stopping(cost, opt_cost, threshold, patience, count):
    """Determines if you should stop training early"""
    if opt_cost - cost < threshold:
        count += 1
    else:
        count = 0

    return count >= patience, count
