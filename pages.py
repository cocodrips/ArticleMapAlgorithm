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


def get_max(page_sets):
    """
    Return:
      (Page)  Get page having highest average of priority.
    """
    if not is_group(page_sets):
        return page_sets

    return max(page_sets, key=lambda p: 1.0 * priority_sum(p) / num(p))

def sort_all(page_sets, reverse=False):
    """
    Sort all pages by priority.

    Return:
      None
    """
    page_sets.sort(key=lambda p:priority_sum(p), reverse=reverse)

    for page_set in page_sets:
        if is_group(page_set):
            sort_all(page_set, reverse=reverse)

def new_sets(page_sets, target):
    """
    Create list without target.
    Objects are not copied.
    """
    pass