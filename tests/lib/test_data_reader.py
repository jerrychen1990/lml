#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/17 3:43 PM
# @Author  : xiaowa

import lml.lib.data_reader as data_reader

def test_read_classify_data():
    items = data_reader.read_classify_data("../../data/perceptron_data/item.csv")
    print(items)

test_read_classify_data()

