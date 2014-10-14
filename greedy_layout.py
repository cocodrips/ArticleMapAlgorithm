# -*- coding: utf-8 -*-
from base import Base
from page_utils import PageUtils
from model.rect_type import rect_types
from model.rect import Rect
import copy
import math


MIN_WIDTH = 100
MIN_HEIGHT = 60

class GreedyLayout(Base):
    def layout(self):
        self._set_ideal_area(self.page_set)
        group_sets = PageUtils.grouping(self.page_set)
        PageUtils.sort(group_sets, reverse=True, key=lambda x: PageUtils.sum(x) / PageUtils.num(x))
        self._arrange(group_sets, Rect(0, 0, self.width, self.height))

    def _set_ideal_area(self, page_sets):
        priority_sum = PageUtils.sum(page_sets)
        area = self.width * self.height
        self._priority_ratio(page_sets, area, priority_sum)

    def _priority_ratio(self, page_sets, area, priority_sum):
        if not PageUtils.is_group(page_sets):
            page_sets.ideal_area = page_sets.priority * area // priority_sum
        else:
            for page_set in page_sets:
                self._priority_ratio(page_set, area, priority_sum)


    def _arrange(self, page_sets, rect):
        if not page_sets:
            return

        elif len(page_sets) < 3:
            self._split(page_sets, rect)

        else:
            self._arrange_top_left(page_sets, rect)

    def _split(self, page_sets, rect):
        if rect.width < rect.height * 1.6:
            self._split_page_sets_area(page_sets, rect, is_vertical=True)
        else:
            self._split_page_sets_area(page_sets, rect, is_vertical=False)


    def _arrange_top_left(self, page_sets, rect):
        tops = PageUtils.max(page_sets)
        remaining_sets = PageUtils.new_sets(page_sets, tops)

        length = len(tops)
        optimal_tops_rect = None
        optimal_sets = []

        min_diff = 1000000000
        ideal_area = PageUtils.ideal_sum(tops)
        is_vertical = False

        for rect_type in rect_types[tops[0].type]:
            if rect_type.min_align > length:
                continue

            # vertical
            diff, bottom_sets, top_rect = (
                self._fix_top_left_rect(remaining_sets, rect, ideal_area, rect_type.ratio / length) )

            if diff < min_diff:
                min_diff = diff
                optimal_tops_rect = top_rect
                optimal_sets = bottom_sets
                is_vertical = True

            # horizontal
            diff, bottom_sets, top_rect = (
                self._fix_top_left_rect(remaining_sets, rect, ideal_area, rect_type.ratio * length) )

            if diff < min_diff:
                min_diff = diff
                optimal_tops_rect = top_rect
                optimal_sets = bottom_sets
                is_vertical = False

        width = (PageUtils.ideal_sum(tops) + PageUtils.ideal_sum(optimal_sets)) / rect.height

        optimal_tops_rect.height = int(optimal_tops_rect.area / width)
        optimal_tops_rect.width = width

        bottom_sets_rect = self._bottom_rect(rect, optimal_tops_rect)
        remaining_rect = copy.deepcopy(rect)
        remaining_rect.x += width
        remaining_rect.width -= width

        for target in optimal_sets:
            remaining_sets = PageUtils.new_sets(remaining_sets, target)

        self._split_page_sets_area(tops, optimal_tops_rect, is_vertical)
        self._arrange(optimal_sets, bottom_sets_rect)
        self._arrange(remaining_sets, remaining_rect)


    def _fix_top_left_rect(self, remaining_sets, parent_rect, ideal_area, ratio):
        top_rect = copy.deepcopy(parent_rect)

        top_rect.height = int(math.sqrt(ideal_area / ratio))
        top_rect.width \
            = int(ratio * top_rect.height)

        bottom_rect = self._bottom_rect(parent_rect, top_rect)
        diff, bottom_sets = self._diff_from_ideal_area(remaining_sets, bottom_rect)

        return diff, bottom_sets, top_rect


    def _diff_from_ideal_area(self, remaining_sets, bottom_rect):
        bottom_sets = PageUtils.get_optimal_set(remaining_sets, bottom_rect)
        closest_area = PageUtils.ideal_sum(bottom_sets)
        return abs(bottom_rect.area - closest_area), bottom_sets

    def _bottom_rect(self, parent_rect, top_rect):
        return Rect(parent_rect.x,
                    parent_rect.y + top_rect.height,
                    top_rect.width,
                    parent_rect.height - top_rect.height)


    def _split_page_sets_area(self, page_sets, rect, is_vertical):
        """
        Args:
            page_sets
            rect
            is_vertcal
        """

        width, height = rect.width, rect.height
        page_sets_ideal_sum = PageUtils.ideal_sum(page_sets)

        is_equally = True
        for page in page_sets:
            if PageUtils.is_group(page):
                is_equally = False
                break

        if is_vertical:
            y = rect.y
            for page in page_sets:
                if is_equally:
                    height = rect.height / len(page_sets)
                else:
                    height = int(rect.height * (PageUtils.ideal_sum(page) / float(page_sets_ideal_sum)))

                page_rect = copy.deepcopy(rect)
                page_rect.y = y
                page_rect.height = height
                y += height

                if PageUtils.is_group(page):
                    self._arrange(page, page_rect)
                else:
                    page.rect = page_rect

        else:
            x = rect.x
            for page in page_sets:
                if is_equally:
                    width = rect.width / len(page_sets)
                else:
                    width = int(rect.width * (PageUtils.ideal_sum(page) / float(page_sets_ideal_sum)))

                page_rect = copy.deepcopy(rect)
                page_rect.x = x
                page_rect.width = width
                x += width

                if PageUtils.is_group(page):
                    self._arrange(page, page_rect)
                else:
                    page.rect = page_rect
