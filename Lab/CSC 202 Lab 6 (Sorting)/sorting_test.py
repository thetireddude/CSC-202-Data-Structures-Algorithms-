import unittest
import selection_sort
import insertion_sort
import quick_sort


class MyTestCase(unittest.TestCase):
    def test_selection_sort(self):
        blah5 = [28, 87, 26, 76, 10, 18, 16, 0, 3, 70]
        selection_sort.selection_sort(blah5)
        sorted_blah5 = [0, 3, 10, 16, 18, 26, 28, 70, 76, 87]
        self.assertEqual(blah5, sorted_blah5)

    def test_insertion_sort(self):
        blah6 = [30, 27, 38, 21, 11, 60, 95, 47, 13, 1]
        insertion_sort.insertion_sort(blah6)
        sorted_blah6 = [1, 11, 13, 21, 27, 30, 38, 47, 60, 95]
        self.assertEqual(blah6, sorted_blah6)

    def test_quick_sort(self):
        blah7 = [82, 26, 37, 93, 7, 78, 39, 25, 87, 79]
        quick_sorted_blah7, comparisons = quick_sort.quick_sort(blah7, 0)
        sorted_blah7 = [7, 25, 26, 37, 39, 78, 79, 82, 87, 93]
        self.assertEqual(quick_sorted_blah7, sorted_blah7)


if __name__ == '__main__':
    unittest.main()
