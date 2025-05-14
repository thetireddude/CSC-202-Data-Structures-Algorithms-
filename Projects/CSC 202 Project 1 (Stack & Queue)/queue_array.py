class QueueArray:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates an empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.items = [None] * capacity  # initializing the queue
        self.num_items = 0  # number of elements in the queue

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        return self.num_items == self.capacity

    def enqueue(self, item):
        """Adds item to the queue"""
        if self.num_items < self.capacity:

            self.items[self.num_items] = item
            self.num_items += 1
            print(self.items)
        else:
            raise IndexError("Queue is full")

    def dequeue(self):
        """Returns the current front of the queue"""
        if not self.is_empty():
            item_return = self.items[0]
            for index, item in enumerate(self.items):
                if index + 1 < self.capacity:
                    self.items[index] = self.items[index + 1]
                    self.items[index + 1] = None
            self.num_items -= 1
            return item_return
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        return self.num_items

q1 = QueueArray(3)

for i in range(3):
    q1.enqueue(i)
    print(q1.items)
