#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/28/17 3:41 PM
# @Author  : xiaowa
import random
from lml.lib.base import pmap
from lml.lib.vector import divide, add
from functools import reduce


def compare_data(data_list, predict_list):
    tp_list = []
    tn_list = []
    fp_list = []
    fn_list = []
    for item, pre_tag in zip(data_list, predict_list):
        tag = item.tag
        if tag >= 0 and pre_tag >= 0:
            tp_list.append(item)
        elif tag >= 0 and pre_tag < 0:
            fn_list.append(item)
        elif tag < 0 and pre_tag >= 0:
            fp_list.append(item)
        else:
            tn_list.append(item)
    return tp_list, tn_list, fp_list, fn_list


def evaluate_data(tp, tn, fp, fn):
    precise = tp * 1.0 / (tp + fp)
    recall = tp * 1.0 / (tp + fn)
    f1_value = f1(precise, recall)
    return precise, recall, f1_value


def f_value(precise, recall, beta):
    recall = recall * beta
    rs = (1.0 + beta) / (1.0 / precise + 1.0 / recall)
    return rs


def f1(precise, recall):
    return f_value(precise, recall, 1.0)


def cut_data(data_set, cut_pre):
    random.shuffle(data_set)
    first_len = int(len(data_set) * cut_pre)
    first_set = data_set[0:first_len]
    second_set = data_set[first_len:]
    return first_set, second_set


def evaluate_simple_classify(algo, data_set, train_per, test_num, **algo_args):
    avg_list = []

    for idx in range(test_num):
        train_set, test_set = cut_data(data_set, train_per)
        test_algo = algo()
        test_algo.load_data(train_set)
        test_algo.train(**algo_args)
        predict_list = pmap(lambda x: test_algo.predict(x.item), test_set)
        tp, tn, fp, fn = compare_data(test_set, predict_list)
        evaluate_value = evaluate_data(len(tp), len(tn), len(fp), len(fn))
        print("test{}, value:{}".format(idx, evaluate_value))
        avg_list.append(list(evaluate_value))
    rs_list = divide(v=reduce(add, avg_list), num=len(avg_list))

    print(rs_list)
