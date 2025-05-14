import unittest
from queue_array import QueueArray

class MyTestCase(unittest.TestCase):
    def test_capacity(self):
        q1 = QueueArray(7)

        self.assertEqual(q1.capacity, 7)

    def test_is_empty(self):
        q2 = QueueArray(7)

        self.assertTrue(q2.is_empty())

    def test_is_full(self):
        q3 = QueueArray(2)
        q3.enqueue(4)
        q3.enqueue(7)

        self.assertTrue(q3.is_full())

    def test_enqueue(self):
        q4 = QueueArray(4)

        for i in range(2):
            q4.enqueue(i)

        self.assertEqual(q4.num_items, 2)

    def test_enqueue_error_handling(self):
        q5 = QueueArray(3)

        for i in range(3):
            q5.enqueue(i)

        self.assertRaises(IndexError, q5.enqueue, 5)

    def test_dequeue(self):
        q6 = QueueArray(4)
        q6.enqueue(6)
        q6.enqueue(17)
        q6.enqueue(9)

        q6.dequeue()
        self.assertEqual(q6.dequeue(), 17)

    def test_dequeue_error_handling(self):
        q7 = QueueArray(3)

        with self.assertRaises(IndexError) as e:
            q7.dequeue()

    def test_peek(self):
        q8 = QueueArray(4)
        q8.enqueue(6)
        q8.enqueue(17)

        self.assertEqual(q8.peek(), 6)

    def test_peek_error_handling(self):
        q9 = QueueArray(3)
        self.assertRaises(IndexError, q9.peek)

    def test_size(self):
        q10 = QueueArray(14)
        q10.enqueue(5)
        q10.enqueue(6)
        q10.enqueue(17)
        q10.enqueue(9)

        self.assertEqual(q10.size(), 4)

if __name__ == '__main__':
    unittest.main()