#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/17 3:28 PM
# @Author  : xiaowa
import random
from lml.lib.mymath import sign


def gen_liner_vec(min_dis, max_dis, min_x, max_x, positive_rate, k, b):
    distance = random.uniform(min_dis, max_dis)
    x = random.uniform(min_x, max_dis)
    x_change = distance * k / (1 + k)
    y_change = distance * -1 / (1 + k)
    if random.random() < positive_rate:
        x_change = -x_change
        y_change = -y_change
    x += y_change
    y = k * x + b
    y += x_change
    z = sign(y_change)
    return x, y, z
