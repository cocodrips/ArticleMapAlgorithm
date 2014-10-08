from base import Base

import pages


class GreedyLayout(Base):
    def layout(self):
        pass

    def _arrange(self, page_sets, rect):
        if not page_sets:
            return

        if len(page_sets) < 3:
            # self.divide_space(page)
            pass

    def _divide_space(self, page_sets, rect):

        pass

    def _arrange_top_1(self, page_sets, rect):
        pass


