#!/usr/bin/env python3
""" L2 regularization cost"""
import tensorflow as tf


def l2_reg_cost(cost, model):
    """ L2 regularization cost """
    if not model.losses:
        return cost
    return cost + tf.convert_to_tensor(model.losses)
