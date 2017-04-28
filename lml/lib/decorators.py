#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/28/17 3:50 PM
# @Author  : xiaowa
import functools
import lml.lib.common as common
import logging


def print_log(logger=common.default_logger, level=logging.INFO):
    def log_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            do_logging_work(logger, level, "{} started".format(func.__name__),  *args, **kwargs)
            rs = func(*args, **kwargs)
            do_logging_work(logger, level, "{} finished".format(func.__name__), result=rs)

        return wrapper

    return log_decorator


def do_logging_work(logger, level, msg, *args, **kwargs):
    _log_fun_dict = {
        logging.INFO: logger.info,
        logging.ERROR: logger.error,
        logging.DEBUG: logger.debug
    }

    def log_func(func):
        func("{}, args:{}, kwargs:{}".format(msg, args, kwargs))

    log_func(_log_fun_dict.get(level, logger.info))

@print_log(level=logging.ERROR)
def func(a, b):
    rs = a + b
    return rs

func(5, b=2)


