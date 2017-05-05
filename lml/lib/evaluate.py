#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/28/17 3:41 PM
# @Author  : xiaowa

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
    return tn_list, tn_list, fp_list, fn_list

def evaluate_data(data_list, predict_list):
    pass



