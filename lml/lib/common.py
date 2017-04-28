#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/28/17 3:45 PM
# @Author  : xiaowa

import logging
LOG_FORMAT = logging.Formatter("%(asctime)s %(name)s [%(levelname)s]  %(filename)s:%(lineno)d - %(message)s")

CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setFormatter(LOG_FORMAT)


default_logger = logging.getLogger("default_logger")
default_logger.addHandler(CONSOLE_HANDLER)
default_logger.setLevel(logging.INFO)




