# -*- coding: utf-8 -*-
from page_utils import PageUtils as utils
import unittest
import page_generator
import os


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.generator = page_generator.PageGenerator()
        self.page_set = self.generator.generate_from_jsonfile(self.path + '/sample/sample1.json')

    def testPrioritySum(self):
        target = utils.sum(self.page_set)
        self.assertEqual(target, 34)

    def testIsGroup(self):
        target = utils.is_group(self.page_set)
        self.assertTrue(target)

    def testNum(self):
        target = utils.num(self.page_set)
        self.assertEqual(target, 7)

    def testGetMax(self):
        target = utils.max(self.page_set)
        self.assertEqual(target[0].priority, 7)

    def testSortAll(self):
        utils.sort(self.page_set)
        self.assertEqual(self.page_set[0][0].priority, 1)
        utils.sort(self.page_set, reverse=True)
        self.assertEqual(self.page_set[0][0].priority, 9)


if __name__ == "__main__":
    unittest.main()
