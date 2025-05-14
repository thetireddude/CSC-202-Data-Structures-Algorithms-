import unittest
from string_checker import string_checker

class MyTestCase(unittest.TestCase):
    def test_balanced_with_none(self):
        self.assertEqual(string_checker("ejueejej"), True)

    def test_balanced_with_several(self):
        self.assertEqual(string_checker("fjggj{djdjd}()wkw[445]"), True)

    def test_unbalanced_with_opening(self):
        self.assertEqual(string_checker("{jejeej{kejt(ekk[wjjeee{("), False)

    def test_unbalanced_with_closing(self):
        self.assertEqual(string_checker("[djejeje}eejeje()02033)]"), False)

    def test_unbalanced_incorrectly_arranged(self):
        self.assertEqual(string_checker("(jjjffjfjf}wkkee]wkeke{[)"), False)

    def test_unbalanced_with_opening_and_pairs(self):
        self.assertEqual(string_checker("(ririrr)}wo(wow{[eo44"), False)

    def test_unbalanced_with_closing_and_pairs(self):
        self.assertEqual(string_checker("]yreh}433{]"), False)


if __name__ == '__main__':
    unittest.main()
