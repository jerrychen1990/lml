#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/27/17 5:57 PM
# @Author  : xiaowa
import math
import pytest
import lml.lib.vector as vector

VEC1 = [1, 2, 0, 4, -3]
VEC2 = [3, 0, -2, 2, 1]

def test_norm():
    assert vector.norm(VEC1, 0) == 4
    assert vector.norm(VEC1, 1) == 10
    assert vector.norm(VEC1, 2) == math.pow(30, 1.0 / 2)
    assert vector.norm(VEC1, 3) == math.pow(100, 1.0 / 3)
    with pytest.raises(ValueError) as err_info:
        vector.norm(VEC1, -1)
    # print(vars(err_info.value))
    # assert err_info.value == 'invalid norm value -1'

    # vector.norm(VEC1, -1)

def test_inner_product():
    assert vector.inner_product(VEC1, VEC2) == 8




