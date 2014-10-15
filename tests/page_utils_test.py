# -*- coding: utf-8 -*-
from page_utils import PageUtils as utils
from model.rect import Rect
import unittest
import page_generator
import os


class PageUtilsTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.generator = page_generator.PageGenerator()
        self.page_set = self.generator.generate_from_jsonfile(self.path + '/sample/sample1.json')
        self.pure_page_set = self.generator.generate_from_jsonfile(self.path + '/sample/pure_sample0.json')

    def testSum(self):
        target = utils.sum(self.page_set)
        self.assertEqual(target, 34)

    def testIsGroup(self):
        target = utils.is_group(self.page_set)
        self.assertTrue(target)

    def testNum(self):
        target = utils.num(self.page_set)
        self.assertEqual(target, 7)

    def testMax(self):
        target = utils.max(self.page_set)
        self.assertEqual(target[0].priority, 7)

    def testSort(self):
        utils.sort(self.page_set)
        self.assertEqual(self.page_set[0][0].priority, 1)
        utils.sort(self.page_set, reverse=True)
        self.assertEqual(self.page_set[0][0].priority, 9)

        self.page_set[1][2].priority = 100
        utils.sort(self.page_set, reverse=True, key=lambda p: utils.avg(p))
        self.assertEqual(self.page_set[0][0].priority, 100)

    def testNewSets(self):
        new_sets = utils.new_sets(self.page_set, self.page_set[0][0])
        target = utils.num(new_sets)

        self.assertEqual(target, 6)
        self.assertEqual(utils.num(self.page_set), 7)

        new_sets[0][0].priority = 100
        self.assertEqual(self.page_set[0][1].priority, 100)

    def testIdealSum(self):
        self.page_set[0][0].ideal_area = 100
        self.page_set[0][1].ideal_area = 123
        target = utils.ideal_sum(self.page_set)
        self.assertEqual(target, 223)

    def testGrouping(self):
        target = utils.grouping(self.pure_page_set)
        self.assertEqual(target[1][1].priority, 2)

    def testGetOptimumSet(self):
        for page in self.pure_page_set:
            page.ideal_area = pow(page.priority * 100, 2)

        target = utils.get_optimal_set(self.pure_page_set, Rect(0, 0, 500, 300))
        self.assertEqual(target[0].priority, 4)

    def testDeformPriorities(self):
        self.assertEqual(self.pure_page_set[0].priority, 10)
        utils.deform_priorities(self.pure_page_set, 800 * 600, 200, 60)
        self.assertEqual(self.pure_page_set[0].priority, 8)


if __name__ == "__main__":
    unittest.main()
