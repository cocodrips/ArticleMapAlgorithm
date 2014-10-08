from greedy_layout import GreedyLayout
import unittest
import os


class BruteForceTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.layout = GreedyLayout(self.path + '/sample/sample0.json')


if __name__ == "__main__":
    unittest.main()
