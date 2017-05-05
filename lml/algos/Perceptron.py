#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/4/17 4:57 PM
# @Author  : xiaowa

import random
from lml.lib.concepts import ClassifyAlgorithm
from lml.lib.mymath import sign
from lml.lib.vector import inner_product
from lml.lib.decorators import pmap
from lml.lib.common import default_logger
from lml.lib.evaluate import compare_data



class Perceptron(ClassifyAlgorithm):
    def __init__(self):
        self.data_list = []
        self.weight_list = []
        self.logger = default_logger

    def load_data(self, data_list):
        self.data_list = data_list

        pass

    def train(self, func=sign, learn_percent=0.1):
        self.weight_list = [0.0] * (len(self.data_list[0].vec) + 1)
        while True:
            predict_list = pmap(lambda x: self.predict(x, func), self.data_list)
            _, _, fp, fn = compare_data(self.data_list, predict_list)
            false_list = fp + fn
            if len(false_list) == 0:
                break
            sample_tag=false_list.



    def predict(self, item, func):
        vec = item.vec
        vec.append(1.0)

        return func(inner_product(vec, self.weight_list))
