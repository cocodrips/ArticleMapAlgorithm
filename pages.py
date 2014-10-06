# -*- coding: utf-8 -*-
import types


def is_group(page_set):
    return type(page_set) == types.ListType


def priority_sum(page_sets):
    """
    Return:
      (int)  Sum of priority of whole of sets.
    """
    if not is_group(page_sets):
        return page_sets.priority
    return sum([priority_sum(page_set) for page_set in page_sets])


def num(page_sets):
    if not is_group(page_sets):
        return 1
    return sum(num(page_set) for page_set in page_sets)


def get_top_1(page_sets):
    """
    Return:
      (Page)  Get page having highest average of priority.
    """
    if not is_group(page_sets):
        return page_sets

    top = page_sets[0]
    top_sum = 0

    for page_set in page_sets:
        s = priority_sum(page_set)
        n = num(page_set)
        if top_sum < 1.0 * s / n:
            top_sum = s
            top = page_set
    return top

