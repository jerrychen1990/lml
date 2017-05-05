#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/4/17 5:33 PM
# @Author  : xiaowa

from lml.lib.concepts import TaggedItem, Item
from lml.lib.data_reader import read_classify_data
from lml.algos.perceptron import Perceptron
import random
import lml.lib.evaluate as evaluate

data_size = 16
vec_list = [[]] * data_size
item_list = map(lambda x: Item(item_id=x[0], vec=x[1]), enumerate(vec_list))

tag_item_list = map(lambda x: TaggedItem(tag=random.randint(-2, 3), item=x), item_list)
predict_list = map(lambda x: random.randint(-4, 4), range(0, data_size))
# print(vec_list)
# print(list(tag_item_list))
# print(list(predict_list))

def test_compare_data():
    tp, tn, fp, fn = evaluate.compare_data(tag_item_list, predict_list)
    print(tp, tn, fp, fn)

def test_cut_data():
    to_cut = list(range(0, 10))
    first, second = evaluate.cut_data(to_cut, 0.5)
    print(first)
    print(second)

def test_evaluate_simple_classify():
    data = read_classify_data("../../data/perceptron_data/item.csv")
    # print(data)
    evaluate.evaluate_simple_classify(Perceptron, data, 0.5, 10, learn_percent=0.01)










# test_compare_data()
test_evaluate_simple_classify()