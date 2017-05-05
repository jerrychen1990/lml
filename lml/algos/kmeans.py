#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/28/17 11:14 AM
# @Author  : xiaowa
import random
import lml.lib.concepts as concepts
import lml.lib.decorators as decorators
import lml.lib.distance as distance
import lml.lib.vector as vector
from lml.lib.common import default_logger as logger
from functools import reduce


class Kmeans(concepts.ClusteringAlgorithm):
    def __init__(self):
        logger.info("kmeans initialized")
        self.data_list = []
        self.cluster_list = []

    @decorators.print_log()
    def load_data(self, data_list):
        self.data_list = data_list

    @decorators.print_log(print_args=True)
    def do_cluster(self, k, max_iter_cnt=100):
        for item in random.sample(self.data_list, k):
            self.cluster_list.append({"center": item.vec, "data": []})

        iter_cnt = 0
        while iter_cnt < max_iter_cnt:
            logger.info("start iter {}".format(iter_cnt))
            for item in self.data_list:
                self.assign_data(item)
            iter_cnt += 1
            old_center = map(lambda x: x["center"], self.cluster_list)
            for cluster in self.cluster_list:
                Kmeans.calculate_center(cluster)
            new_center = map(lambda x: x["center"], self.cluster_list)
            if Kmeans.is_convergence(old_center, new_center):
                break
        return self.cluster_list

    def get_clusters(self):
        pass


    @staticmethod
    # @decorators.print_log(print_args=True)
    def is_convergence(old_center, new_center):
        for a, b in zip(old_center, new_center):
            if a != b:
                return False
        return True

    def assign_data(self, item):
        assign_cluster = max(self.cluster_list, key=lambda c: distance.cosine_distance(c["center"], item.vec))
        assign_cluster["data"].append(item)

    @staticmethod
    def calculate_center(item):
        sum_vec = reduce(vector.add, map(lambda x:x.vec, item["data"]))
        center_vec = vector.divide(sum_vec, len(item))
        item["center"] = center_vec
