#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/4/17 4:57 PM
# @Author  : xiaowa

import random
from lml.lib.concepts import ClassifyAlgorithm
from lml.lib.mymath import sign
from lml.lib.vector import inner_product, add, multiply
from lml.lib.base import pmap
from lml.lib.common import default_logger
from lml.lib.evaluate import compare_data


class Perceptron(ClassifyAlgorithm):
    def __init__(self):
        self.data_list = []
        self.weight_list = []
        self.logger = default_logger
        self.func = sign


    def load_data(self, data_list):
        self.data_list = data_list

        pass

    def train(self, func=sign, learn_percent=0.1):
        self.weight_list = [0.0] * (len(self.data_list[0].item.vec) + 1)
        iter_cnt = 0
        while True:
            self.logger.debug("iter{}, weight list:{}".format(iter_cnt, self.weight_list))

            predict_list = pmap(lambda x: self.predict(x.item), self.data_list)
            _, _, fp, fn = compare_data(self.data_list, predict_list)
            false_list = fp + fn
            self.logger.debug("iter{}, false list:{}".format(iter_cnt, false_list))
            self.logger.debug("false list size:{}".format(len(false_list)))
            if len(false_list) == 0:
                self.logger.info("with {} iterators, get weight_list:{}".format(iter_cnt, self.weight_list))
                break
            sample_tag = random.choice(false_list)
            self.weight_list = add(self.weight_list,
                                   multiply(num=sample_tag.tag * learn_percent, vec=sample_tag.item.vec+[1.0]))
            iter_cnt += 1

    def predict(self, item):
        vec = item.vec + [1.0]

        return self.func(inner_product(vec, self.weight_list))
