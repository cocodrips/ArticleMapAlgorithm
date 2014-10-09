# -*- coding: utf-8 -*-
import types


class PageUtils(object):
    @classmethod
    def is_group(cls, page_set):
        return type(page_set) == types.ListType

    @classmethod
    def sum(cls, page_sets):
        """
        Return:
          (int)  Sum of priority of whole of sets.
        """
        if not cls.is_group(page_sets):
            return page_sets.priority
        return sum([cls.sum(page_set) for page_set in page_sets])

    @classmethod
    def num(cls, page_sets):
        if not cls.is_group(page_sets):
            return 1
        return sum(cls.num(page_set) for page_set in page_sets)

    @classmethod
    def max(cls, page_sets):
        """
        Return:
          (Page)  Get page having highest average of priority.
        """
        if not cls.is_group(page_sets):
            return page_sets

        return max(page_sets, key=lambda p: float(cls.sum(p)) / cls.num(p))

    @classmethod
    def sort(cls, page_sets, reverse=False):
        """
        Sort all pages by priority.

        Return:
          None
        """
        page_sets.sort(key=lambda p: cls.sum(p), reverse=reverse)

        for page_set in page_sets:
            if cls.is_group(page_set):
                cls.sort(page_set, reverse=reverse)
    @classmethod
    def new_sets(cls, l, target):
        return l if not cls.is_group(l) else [cls.new_sets(i, target) for i in l if i != target]


