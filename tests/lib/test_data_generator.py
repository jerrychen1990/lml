#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/17 3:33 PM
# @Author  : xiaowa

import lml.lib.data_generator as data_generator

for i in range(100):
    item = data_generator.gen_liner_vec(0, 15, -50, 20, 0.4, 2, -4)

    print(",".join(map(lambda x: str(x), item)))

