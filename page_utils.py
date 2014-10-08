# -*- coding: utf-8 -*-
import types


class PageUtils(object):
    @classmethod
    def is_group(cls, page_set):
        return type(page_set) == types.ListType

    @classmethod
    def priority_sum(cls, page_sets):
        """
        Return:
          (int)  Sum of priority of whole of sets.
        """
        if not cls.is_group(page_sets):
            return page_sets.priority
        return sum([cls.priority_sum(page_set) for page_set in page_sets])

    @classmethod
    def num(cls, page_sets):
        if not cls.is_group(page_sets):
            return 1
        return sum(cls.num(page_set) for page_set in page_sets)

    @classmethod
    def get_max(cls, page_sets):
        """
        Return:
          (Page)  Get page having highest average of priority.
        """
        if not cls.is_group(page_sets):
            return page_sets

        return max(page_sets, key=lambda p: float(cls.priority_sum(p)) / cls.num(p))

    @classmethod
    def sort_all(cls, page_sets, reverse=False):
        """
        Sort all pages by priority.

        Return:
          None
        """
        page_sets.sort(key=lambda p: cls.priority_sum(p), reverse=reverse)

        for page_set in page_sets:
            if cls.is_group(page_set):
                cls.sort_all(page_set, reverse=reverse)

    @classmethod
    def new_sets(cls, page_sets, target):
        """
        Create list without target.
        Objects are not copied.
        """
        pass
