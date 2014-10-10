# -*- coding: utf-8 -*-
from model.rect_type import rect_types
import math
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

    @classmethod
    def ideal_sum(cls, page_sets):
        if not cls.is_group(page_sets):
            return page_sets.ideal_area
        return sum([cls.ideal_sum(page_set) for page_set in page_sets])

    @classmethod
    def grouping(cls, page_sets, range=1.4):
        """
        Grouping only a list of page_sets 
        """
        groups = []

        for rect_type in rect_types:
            target_sets = [page_set for page_set in page_sets if page_set.type == rect_type]
            PageUtils.sort(target_sets)

            while target_sets:
                base = target_sets.pop(0)
                group = [base]

                if target_sets and \
                        target_sets[0].priority <= int(math.ceil(base.priority * range)):
                    pair = target_sets.pop(0)
                    group.append(pair)
                groups.append(group)

        return groups



