from greedy_layout import GreedyLayout
from model.rect import Rect
from page_utils import PageUtils
import unittest
import os


class GreedyLayoutTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.layout = GreedyLayout(self.path + '/sample/sample0.json', 800, 600)

    def testSetIdealArea(self):
        self.layout._set_ideal_area(self.layout.page_set)
        self.assertEqual(self.layout.page_set[0].ideal_area, 138461)

if __name__ == "__main__":
    unittest.main()
