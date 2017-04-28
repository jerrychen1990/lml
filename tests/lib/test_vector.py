#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/27/17 5:57 PM
# @Author  : xiaowa
import math
import pytest
import lml.lib.vector as vector

VEC1 = [1, 2, 0, 4, -3]
VEC2 = [3, 0, -2, 2, 1]
VEC3 = [2, 4, 9]

def test_norm():
    assert vector.norm(VEC1, 0) == 4
    assert vector.norm(VEC1, 1) == 10
    assert vector.norm(VEC1, 2) == math.pow(30, 1.0 / 2)
    assert vector.norm(VEC1, 3) == math.pow(100, 1.0 / 3)
    with pytest.raises(ValueError) as err_info:
        vector.norm(VEC1, -1)
    assert str(err_info.value) == 'invalid norm value -1'


def test_inner_product():
    assert vector.inner_product(VEC1, VEC2) == 8
    with pytest.raises(ValueError) as err_info:
        vector.inner_product(VEC1, VEC3)
    assert str(err_info) == 'different vector length: 5, 3'






