# -*- coding: utf-8 -*-
import types


def is_group(page_set):
    return type(page_set) == types.ListType


def priority_sum(page_sets):
    """
    Return:
      int: Sum of priority of whole of sets.
    """
    if not is_group(page_sets):
        return page_sets.priority
    return sum([priority_sum(page_set) for page_set in page_sets])

