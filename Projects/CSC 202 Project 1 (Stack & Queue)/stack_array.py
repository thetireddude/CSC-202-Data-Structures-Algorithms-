class StackArray:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity  # Capacity of your stack
        self.items = [None] * capacity  # initializing the stack
        self.num_items = 0  # number of elements in the stack

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        return self.num_items == self.capacity

    def push(self, item):
        """Adds item to the stack"""
        if self.num_items < self.capacity:
            self.items[self.num_items - 1] = item
            self.num_items += 1
        else:
            raise IndexError("Stack is full")

    def pop(self):
        """Returns the current top of the stack"""
        if not self.is_empty():
            for index, item in enumerate(self.items):
                if item is None or item == self.items[-1]:
                    self.num_items -= 1
                    return_value = self.items[index -1]
                    self.items[index - 1] = None
                    return return_value
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        """Returns the value of the item at the top of the stack without removing it"""
        if not self.is_empty():
            for index, item in enumerate(self.items):
                if item is None or item == self.items[-1]:
                    self.num_items -= 1
                    return_value = self.items[index -1]
                    return return_value
        else:
            raise IndexError("Stack is empty")

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items
