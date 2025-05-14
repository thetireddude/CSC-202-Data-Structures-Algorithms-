import unittest

from binary_search_tree import BinarySearchTree


class MyTestCase(unittest.TestCase):
    def test_is_empty(self):
        t1 = BinarySearchTree()

        self.assertTrue(t1.is_empty())

    def test_insert(self):
        t1 = BinarySearchTree()
        t1.insert(45)
        t1.insert(23)
        t1.insert(55)

        self.assertEqual(t1.num_items, 3)

    def test_find(self):
        t1 = BinarySearchTree()
        t1.insert(45)
        t1.insert(23)
        t1.insert(55)

        self.assertTrue(t1.find(23, t1.root))
        self.assertFalse(t1.find(34, t1.root))

    def test_find_min(self):
        t1 = BinarySearchTree()
        t1.insert(45)
        t1.insert(23)
        t1.insert(55)
        t1.insert(13)   # 13 is the minimum
        t1.insert(43)

        self.assertEqual(t1.find_min(), 13)

    def test_find_max(self):
        t1 = BinarySearchTree()
        t1.insert(43)
        t1.insert(23)
        t1.insert(55)   # 55 is the maximum
        t1.insert(13)
        t1.insert(45)

        self.assertEqual(t1.find_max(), 55)

    def test_delete_leaf(self):
        t1 = BinarySearchTree()
        t1.insert(7)
        t1.insert(11)
        t1.insert(5)
        t1.insert(2)
        t1.insert(6)    # 6 has no children; it is a leaf

        t1.delete(6)

        self.assertEqual(t1.num_items, 4)

    def test_delete_node_single_child(self):
        t1 = BinarySearchTree()
        t1.insert(7)
        t1.insert(11)   # 11 has a single child --> 12
        t1.insert(12)
        t1.insert(5)
        t1.insert(2)
        t1.insert(6)

        t1.delete(11)

        self.assertEqual(t1.num_items, 5)

    def test_delete_node_with_two_children(self):
        t1 = BinarySearchTree()
        t1.insert(7)
        t1.insert(11)
        t1.insert(5)    # 5 has two children --> 2 and 6
        t1.insert(2)
        t1.insert(6)

        t1.delete(5)

        self.assertEqual(t1.num_items, 4)


if __name__ == '__main__':
    unittest.main()
