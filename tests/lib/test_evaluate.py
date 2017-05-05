#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/4/17 5:33 PM
# @Author  : xiaowa

from lml.lib.concepts import TaggedItem, Item
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


# test_compare_data()

print([1,3,4] + [0,4])