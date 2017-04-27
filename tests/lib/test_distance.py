#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/27/17 9:44 PM
# @Author  : xiaowa

import math
import lml.lib.distance as distance

VEC1 = [3, 0, -4]
VEC2 = [0, 0, 10]


def test_cosine_distance():
    assert distance.cosine_distance(VEC1, VEC2) == -0.8
