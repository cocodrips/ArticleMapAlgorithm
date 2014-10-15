from greedy_layout import GreedyLayout
from display import Display
import unittest
import os


class DisplayTest(unittest.TestCase):
    def setUp(self):
        filepath = os.path.dirname(os.path.abspath(__file__)) + '/sample/sample0.json'
        layout = GreedyLayout(filepath, 800, 600)
        self.display = Display(layout)

    def testShow(self):
        self.display.show()

    def testSomeCase(self):
        self.case1()

    def case1(self):
        filepath = os.path.dirname(os.path.abspath(__file__)) + '/sample/sample2.json'
        layout = GreedyLayout(filepath, 800, 600)
        self.display = Display(layout)
        self.display.show()




if __name__ == "__main__":
    unittest.main()
