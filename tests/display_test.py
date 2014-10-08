from greedy_layout import GreedyLayout
from display import Display
import unittest
import os


class DisplayTest(unittest.TestCase):
    def setUp(self):
        filepath = os.path.dirname(os.path.abspath(__file__)) + '/sample/sample0.json'
        layout = GreedyLayout(filepath, 1000, 800)
        self.display = Display(layout)

    def testShow(self):
        self.display.show()


if __name__ == "__main__":
    unittest.main()
