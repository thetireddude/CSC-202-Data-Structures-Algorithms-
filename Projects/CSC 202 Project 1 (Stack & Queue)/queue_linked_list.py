class QueueLinkedList:
    """Implements an efficient first-in first-out Abstract Data Type using a linked List"""

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __str__(self):
        output = ""
        current = self.head
        i = 0
        while i < self.capacity:
            if current is None:
                output += f"[]"
            else:
                output += f"[{current.item}]"
                current = current.next
            i += 1
        return output

    def __init__(self, capacity):
        """Creates and empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.head = None  # expect an instance of type Node - This is the starting point of the linked list
        self.num_items = 0  # number of elements in the queue

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        return self.num_items == self.capacity

    def enqueue(self, item):
        """Adds item to the queue"""
        if not self.is_full():
            new_node = self.Node(item)
            new_node.next = self.head
            self.head = new_node
            self.num_items += 1
        else:
            raise IndexError("Queue is full")

    def dequeue(self):
        """Returns the current front of the queue"""
        if not self.is_empty():

            old_tail_node = self.head
            while old_tail_node.next:
                old_tail_node = old_tail_node.next

            new_tail_node = self.head
            for x in range(0, self.num_items - 2):
                new_tail_node = new_tail_node.next
            new_tail_node.next = None
            self.num_items -= 1

            return old_tail_node.item
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        if not self.is_empty():
            node_to_peek = self.head
            while node_to_peek.next is not None:
                node_to_peek = node_to_peek.next
            return node_to_peek.item
        raise IndexError("Queue is empty")

    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        return self.num_items

