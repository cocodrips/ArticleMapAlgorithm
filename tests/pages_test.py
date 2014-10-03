# -*- coding: utf-8 -*-
import unittest
import page_generator
import pages
import os


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.generator = page_generator.PageGenerator()
        self.page_set = self.generator.generate_from_json(self.path + '/sample/sample1.json')

    def testPrioritySum(self):
        target = pages.priority_sum(self.page_set)
        self.assertEqual(target, 34)

    def testIsGroup(self):
        target = pages.is_group(self.page_set)
        self.assertTrue(target)


if __name__ == "__main__":
    unittest.main()