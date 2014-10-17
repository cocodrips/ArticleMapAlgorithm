from greedy_layout import GreedyLayout
from display import Display
import unittest
import os
from model.rect_type import rect_types
from page_utils import PageUtils


class DisplayTest(unittest.TestCase):
    def setUp(self):
        filepath = os.path.dirname(os.path.abspath(__file__)) + '/sample/sample0.json'
        layout = GreedyLayout(filepath, 800, 600)
        self.display = Display(layout)

    def testShow(self):
        self.display.show()

    def testSomeCase(self):
        self.case1()
        self.case2()

    def case1(self):
        filepath = os.path.dirname(os.path.abspath(__file__)) + '/sample/sample2.json'
        layout = GreedyLayout(filepath, 1500, 1000)
        self.display = Display(layout)
        self.display.show()
        self.score(layout)


    def case2(self):
        filepath = os.path.dirname(os.path.abspath(__file__)) + '/sample/sample5.json'
        layout = GreedyLayout(filepath, 1500, 1000)

        self.display = Display(layout)
        self.display.show()
        self.score(layout)

    def score(self,layout):

        diff_ratio = 0
        min_ratio = 0
        diff_scale = 0
        for page in layout.page_set:
            # print page.rect
            r = float(page.rect.width) / page.rect.height

            mini = 100
            for t in rect_types[page.type]:
                if r < t.ratio:
                    mini = min(mini, t.ratio / r)
                else:
                    mini = min(mini, r / t.ratio)

            min_ratio = max(min_ratio, mini * mini - 1)
            diff_ratio += mini * mini - 1

        print "diff ratio:", diff_ratio, "min:", min_ratio
        print "diff scale", diff_scale






if __name__ == "__main__":
    unittest.main()
