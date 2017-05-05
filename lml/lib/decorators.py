#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/28/17 3:50 PM
# @Author  : xiaowa
import functools
import lml.lib.common as common
import logging


def print_log(logger=common.default_logger, level=logging.INFO, print_args=False):
    def log_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            do_logging_work(logger, level, print_args, "{} started".format(func.__name__), *args, **kwargs)
            rs = func(*args, **kwargs)
            do_logging_work(logger, level, print_args, "{} finished".format(func.__name__), result=rs)
            return rs
        return wrapper

    return log_decorator


def do_logging_work(logger, level, print_args, msg, *args, **kwargs):
    _log_fun_dict = {
        logging.INFO: logger.info,
        logging.ERROR: logger.error,
        logging.DEBUG: logger.debug
    }
    log_msg = msg
    if print_args:
        log_msg = "{}, args:{}, kwargs:{}".format(log_msg, args, kwargs)

    def log_func(func):
        func(log_msg)

    log_func(_log_fun_dict.get(level, logger.info))



