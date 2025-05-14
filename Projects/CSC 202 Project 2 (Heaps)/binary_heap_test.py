import unittest
from binary_heap import BinHeap


class MyTestCase(unittest.TestCase):
    def test_heap_creation(self):
        h1 = BinHeap(30)
        self.assertEqual(len(h1.collection), 30)
        self.assertEqual(h1.num_items, 0)

    def test_is_empty(self):
        h1 = BinHeap(10)

        self.assertTrue(h1.is_empty())

    def test_insert(self):
        h1 = BinHeap(3)
        h1.insert(5)

        self.assertEqual(h1.__str__(), " 5")

    def test_insert_when_full(self):
        h1 = BinHeap(2)
        h1.insert(10)
        h1.insert(7)
        h1.insert(11)

        self.assertEqual(h1.size, 4)

    def test_delete(self):
        h1 = BinHeap(10)
        h1.insert(6)
        h1.insert(11)
        h1.insert(67)
        h1.insert(8)

        self.assertEqual(h1.deleteMin(), 6)

    def test_delete_exception_handling(self):
        h1 = BinHeap(10)

        with self.assertRaises(h1.MyException) as e:
            h1.deleteMin()
        self.assertEqual(str(e.exception), "Heap is empty")

    def test_size(self):
        h1 = BinHeap(10)

        for i in range(7):
            h1.insert(i ** 7)

        self.assertEqual(h1.collection_size(), 7)





if __name__ == '__main__':
    unittest.main()
