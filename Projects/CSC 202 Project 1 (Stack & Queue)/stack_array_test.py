import unittest
from stack_array import StackArray


class MyTestCase(unittest.TestCase):

    def test_capacity(self):
        s1 = StackArray(7)

        self.assertEqual(s1.capacity, 7)

    def test_is_empty(self):
        s2 = StackArray(4)
        self.assertTrue(s2.is_empty())

    def test_is_full(self):
        s3 = StackArray(2)
        s3.push(3)
        s3.push(7)

        self.assertTrue(s3.is_full())

    def test_push(self):
        s4 = StackArray(6)

        s4.push(6)
        s4.push(1)

        self.assertEqual(s4.num_items, 2)

    def test_push_error_handling(self):
        s5 = StackArray(3)
        s5.push(6)
        s5.push(17)
        s5.push(9)

        with self.assertRaises(IndexError) as e:
            s5.push(12)
        self.assertEqual(str(e.exception), "Stack is full")

    def test_pop(self):
        s6 = StackArray(3)

        s6.push(4)
        s6.push(7)
        s6.push(1)

        self.assertEqual(s6.pop(), 1)

    def test_pop_error_handling(self):
        s7 = StackArray(2)

        with self.assertRaises(IndexError) as e:
            s7.pop()
        self.assertEqual(str(e.exception), "Stack is empty")

    def test_peek(self):
        s8 = StackArray(2)
        s8.push(4)
        s8.push(3)

        self.assertEqual(s8.peek(), 3)

    def test_peek_error_handling(self):
        s9 = StackArray(2)

        with self.assertRaises(IndexError) as e:
            s9.peek()
        self.assertEqual(str(e.exception), "Stack is empty")

    def test_size(self):
        s10 = StackArray(4)
        s10.push(7)
        s10.push(9)
        s10.push(4)

        self.assertEqual(s10.size(), 3)




if __name__ == '__main__':
    unittest.main()
