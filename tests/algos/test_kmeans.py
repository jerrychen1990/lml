#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/3/17 3:02 PM
# @Author  : xiaowa
import lml.algos.kmeans as kmeans
from lml.lib.concepts import Item
from lml.lib.decorators import pmap

kmeans = kmeans.Kmeans()

train_data = [[0, 10, 20],
              [15, 33, 22],
              [2, 100, 100],
              [-5, 90, 90]]

train_data = pmap(lambda x: Item(x[0], x[1]), enumerate(train_data))
# print(train_data)


kmeans.load_data(train_data)
clusters = kmeans.do_cluster(2)
print("cluster", clusters)
