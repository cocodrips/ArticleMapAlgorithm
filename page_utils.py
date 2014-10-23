# -*- coding: utf-8 -*-
from model.rect_type import rect_types
import itertools
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
    def avg(cls, page_sets):
        """
        Return:
          (int)  Sum of priority of whole of sets.
        """
        return cls.sum(page_sets) // cls.num(page_sets)

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
    def sort(cls, page_sets, reverse=False, key=None):
        """
        Sort all pages by priority.

        Return:
          None
        """
        if not key:
            key = lambda p: cls.sum(p)
        page_sets.sort(key=key,
                       reverse=reverse)

        for page_set in page_sets:
            if cls.is_group(page_set):
                cls.sort(page_set, reverse=reverse, key=key)

    @classmethod
    def new_sets(cls, l, target):
        return l if not cls.is_group(l) else [cls.new_sets(i, target) for i in l if i != target]

    @classmethod
    def ideal_sum(cls, page_sets):
        if not cls.is_group(page_sets):
            return page_sets.ideal_area
        return sum([cls.ideal_sum(page_set) for page_set in page_sets])

    @classmethod
    def grouping(cls, page_sets, range=1.3):
        """
        Grouping only aa  list of page_sets
        """
        page_sets = page_sets[:]

        top = page_sets.pop(0)
        groups = [[top]]

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

    @classmethod
    def get_optimal_set(cls, page_sets, rect):
        # TODO:Refactoring

        s = rect.width * rect.height
        match = 0
        optimum_set = None

        for page_set in page_sets:
            area_sum = PageUtils.ideal_sum(page_set)
            if not optimum_set or abs(s - area_sum) < abs(s - match):
                optimum_set = [page_set]
                match = area_sum

        for a, b in itertools.combinations(page_sets, 2):
            area_sum = PageUtils.ideal_sum(a) + PageUtils.ideal_sum(b)

            if abs(s - area_sum) < abs(s - match):
                optimum_set = [a, b]
                match = area_sum

        return optimum_set

    @classmethod
    def deform_priorities(cls, page_sets, area, min_width, min_height):
        priority_sum = cls.sum(page_sets)
        area_min = min_width * min_height
        x = float(area / area_min) / priority_sum

        for page_set in page_sets:
            if cls.is_group(page_set):
                for page in page_set:
                    page.priority = math.ceil(math.log((math.ceil(x * page.priority)), 2))

            else:
                page_set.priority = math.ceil(math.log((math.ceil(x * page_set.priority)), 2))
