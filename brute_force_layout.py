from base import Base
from page_utils import PageUtils
import itertools

class BruteForceLayout(Base):
    def layout(self, rect, page_set, is_grouping=False):
        if is_grouping:
            self.grouping()


