#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/28/17 5:26 PM
# @Author  : xiaowa
from lml.lib.common import default_logger as logger
import lml.lib.decorators as decorators


class Item:
    def __init__(self, item_id, vec):
        self.item_id = item_id
        self.vec = vec

    def __repr__(self):
        return str(self.__dict__)


class TaggedItem:
    def __init__(self, tag, item):
        self.tag = tag
        self.item = item

    def __repr__(self):
        return str(self.__dict__)


class ClassifyAlgorithm:
    def __init__(self):
        logger.info(self.__name__, "initialized")

    @decorators.print_log()
    def load_data(self, data_list):
        pass


class ClusteringAlgorithm:
    def __init__(self):
        logger.info(self.__name__, "initialized")

    @decorators.print_log()
    def load_data(self, data_list):
        pass

    def get_clusters(self):
        pass

    @decorators.print_log(print_args=True)
    def do_cluster(self, *args, **kwargs):
        pass
