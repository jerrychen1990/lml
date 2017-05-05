#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/17 3:06 PM
# @Author  : xiaowa


import lml.algos.perceptron as perceptron
from lml.lib.data_reader import read_classify_data

train_set = read_classify_data("../../data/perceptron_data/item.csv")
perc = perceptron.Perceptron()
perc.load_data(train_set)
perc.train(learn_percent=0.1)












