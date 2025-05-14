import unittest
from stack_linked_list import StackLinkedList



class MyTestCase(unittest.TestCase):
    def test_capacity(self):
        stack = StackLinkedList(5)                     # creates a stack with capacity of 5
        self.assertEqual(stack.capacity, 5)    # verifies if capacity is 5

    def test_is_empty(self):
        stack = StackLinkedList(3)
        self.assertTrue(stack.is_empty())

    def test_is_full(self):
        stack2 = StackLinkedList(3)
        stack2.push(3)
        stack2.push(6)
        stack2.push(9)

        self.assertTrue(stack2.is_full())

    def test_push(self):
        stack = StackLinkedList(3)
        stack.push(3)
        stack.push(6)
        stack.push(9)

        self.assertEqual(stack.num_items, 3)

    def test_push_error_handling(self):
        stack = StackLinkedList(2)
        stack.push(4)
        stack.push(9)

        with self.assertRaises(IndexError) as e:
            stack.push(5)

        self.assertEqual(str(e.exception), "Stack is full")

    def test_pop(self):
        stack = StackLinkedList(3)
        stack.push(5)
        stack.push(9)
        stack.push(1)

        self.assertEqual(stack.pop(), 1)

    def test_pop_error_handling(self):
        stack = StackLinkedList(3)

        with self.assertRaises(IndexError) as e:
            stack.pop()

        self.assertEqual(str(e.exception), "Stack is empty")

    def test_peek(self):
        stack = StackLinkedList(2)

        stack.push(3)
        stack.push(6)

        self.assertEqual(stack.peek(), 6)

    def test_peek_error_handling(self):
        stack = StackLinkedList(3)

        self.assertRaises(IndexError, stack.peek)

    def test_size(self):
        stack = StackLinkedList(3)

        stack.push(1)
        stack.push(2)

        self.assertEqual(stack.size(), 2)



if __name__ == '__main__':
    unittest.main()
