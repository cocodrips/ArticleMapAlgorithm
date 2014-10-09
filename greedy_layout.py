from base import Base
from page_utils import PageUtils
from model.rect_type import rect_types
import math


class GreedyLayout(Base):
    def layout(self):
        self._set_ideal_area()
        pass

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

        if len(page_sets) < 3:
            # self.divide_space(page)
            pass

    def _divide_space(self, page_sets, rect):
        pass

    def _arrange_top_1(self, page_sets, rect):
        top = PageUtils.max(page_sets)
        new_sets = PageUtils.new_sets(page_sets, top)

        length = len(top)

        for rect_type in rect_types[top.type]:
            if rect_type.min_align > length:
                continue





