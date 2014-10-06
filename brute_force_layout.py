from base import Base

class BruteForceLayout(Base):
    def layout(self, is_grouping=False):
        if is_grouping:
            self.grouping()
        print self.page_set

    def grouping(self):
        pass