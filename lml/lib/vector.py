#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/27/17 4:54 PM
# @Author  : xiaowa
import math
from lml.lib.decorators import persist


def l0(vec):
    return norm(vec, 0)


def l1(vec):
    return norm(vec, 1)


def l2(vec):
    return norm(vec, 2)


def norm(vec, n):
    if n == 0:
        non_zero = list(filter(lambda x: x != 0, vec))
        return len(non_zero)
    if n >= 1:
        sum_value = sum(map(lambda x: math.pow(abs(x), n), vec))
        return math.pow(sum_value, 1.0 / n)
    else:
        raise ValueError("invalid norm value {}".format(n))


def inner_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("different vector length: {}, {}".format(len(v1), len(v2)))
    return sum(map(lambda x: x[0] * x[1], zip(v1, v2)))


@persist
def add(v1, v2):
    return map(lambda x: x[0] + x[1], zip(v1, v2))


@persist
def divide(v, num):
    return map(lambda x: x * 1.0 / num, v)
