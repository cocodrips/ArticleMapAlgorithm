# -*- coding: utf-8 -*-
import unittest
import page_generator
import pages
import os


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.generator = page_generator.PageGenerator()
        self.page_set = self.generator.generate_from_jsonfile(self.path + '/sample/sample1.json')

    def testPrioritySum(self):
        target = pages.priority_sum(self.page_set)
        self.assertEqual(target, 34)

    def testIsGroup(self):
        target = pages.is_group(self.page_set)
        self.assertTrue(target)

    def testNum(self):
        target = pages.num(self.page_set)
        self.assertEqual(target, 7)

    def testGetTop1(self):
        target = pages.get_top_1(self.page_set)
        self.assertEqual(target[0].priority, 10)

    def testSortAll(self):
        pages.sort_all(self.page_set)
        self.assertEqual(self.page_set[0][0].priority, 1)
        pages.sort_all(self.page_set, reverse=True)
        self.assertEqual(self.page_set[0][0].priority, 9)


if __name__ == "__main__":
    unittest.main()
