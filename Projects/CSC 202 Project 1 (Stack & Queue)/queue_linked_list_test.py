import unittest
from queue_linked_list import QueueLinkedList

class MyTestCase(unittest.TestCase):
    def test_capacity(self):
        q1 = QueueLinkedList(4)
        self.assertEqual(q1.capacity, 4)  # add assertion here

    def test_is_empty(self):
        q2 = QueueLinkedList(2)
        self.assertTrue(q2.is_empty())

    def test_is_full(self):
        q3 = QueueLinkedList(4)
        q3.enqueue(4)
        q3.enqueue(7)
        q3.enqueue(1)
        q3.enqueue(13)

        self.assertTrue(q3.is_full())

    def test_enqueue(self):
        q4 = QueueLinkedList(3)
        q4.enqueue(5)
        q4.enqueue(9)

        self.assertEqual(q4.num_items, 2)

    def test_enqueue_error_handling(self):
        q5 = QueueLinkedList(2)
        q5.enqueue(6)
        q5.enqueue(9)

        with self.assertRaises(IndexError) as e:
            q5.enqueue(10)
        self.assertEqual(str(e.exception), "Queue is full")

    def test_dequeue(self):
        q6 = QueueLinkedList(4)
        q6.enqueue(7)
        q6.enqueue(2)
        q6.enqueue(25)

        self.assertEqual(q6.dequeue(), 7)

    def test_dequeue_error_handling(self):
        q7 = QueueLinkedList(4)

        with self.assertRaises(IndexError) as e:
            q7.dequeue()
        self.assertEqual(str(e.exception), "Queue is empty")

    def test_peek(self):
        q8 = QueueLinkedList(3)
        q8.enqueue(5)
        q8.enqueue(21)

        self.assertEqual(q8.peek(), 5)

    def test_peek_error_handling(self):
        q9 = QueueLinkedList(5)

        self.assertRaises(IndexError, q9.peek)

    def test_size(self):
        q10 = QueueLinkedList(4)
        q10.enqueue(67)
        q10.enqueue(5)
        q10.enqueue(17)

        self.assertEqual(q10.size(), 3)
if __name__ == '__main__':
    unittest.main()
