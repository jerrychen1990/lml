#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/5/17 3:37 PM
# @Author  : xiaowa

import codecs
from lml.lib.concepts import TaggedItem, Item
from lml.lib.base import pmap


def read_classify_data(data_path):
    items = []

    with codecs.open(data_path, encoding="utf8") as src:
        for idx, line in enumerate(src):
            line = line.strip()
            fields = line.split(",")
            item = Item(item_id=idx, vec=pmap(float, fields[:-1]))
            tagged_item = TaggedItem(tag=int(fields[-1]), item=item)
            items.append(tagged_item)
    return items
