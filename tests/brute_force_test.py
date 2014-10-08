from brute_force_layout import BruteForceLayout
import unittest
import os

class BruteForceTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.brute_force_layout = BruteForceLayout(self.path + '/sample/sample3.json')


    def testLayout(self):
        self.brute_force_layout.layout()

    def testCombination(self):
        self.brute_force_layout.combination(self.brute_force_layout.page_set)


if __name__ == "__main__":
    unittest.main()
