#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/27/17 4:52 PM
# @Author  : xiaowa

import sys
import lml.lib.vector as vector


def cosine_distance(v1, v2):
    product = vector.inner_product(v1, v2)
    rs = product / (vector.l2(v1) * vector.l2(v2))
    return rs
