import unittest
import page_generator
import os

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.generator = page_generator.PageGenerator()

    def testParse(self):
        page_set = self.generator.generate_from_jsonfile(self.path + '/sample/sample1.json')
        self.assertEqual(len(page_set[1][2]), 2)


if __name__ == "__main__":
    unittest.main()
