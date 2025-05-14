class BinHeap:

    class MyException(Exception):
        def __init__(self, message):
            self.message = message


    def __init__(self, array_size):
        self.collection  = [None] * array_size
        self.size = array_size
        self.num_items = 0

    def __str__(self):
        output = ""
        for element in self.collection:
            if element is not None:
                output += f" {element}"

        return output

    def helper_is_full(self):
        return self.num_items == self.size

    def is_empty(self):
        return self.num_items == 0

    def insert(self, element):
        if self.helper_is_full():
            old_collection = self.collection
            self.size = self.size * 2

            self.collection = [None] * self.size

            for idx, element in enumerate(old_collection):
                self.collection[idx] = element

        self.collection[self.num_items] = element
        self.num_items += 1

        self.helper_restore_heap_property_insert(self.num_items)


    def helper_restore_heap_property_insert(self, num_items):
        idx = num_items - 1
        parent_idx = (idx // 2)

        while parent_idx >= 0 and self.collection[idx] < self.collection[parent_idx]:
            temp = self.collection[parent_idx]
            self.collection[parent_idx] = self.collection[idx]
            self.collection[idx] = temp

            idx = parent_idx
            parent_idx = idx // 2

    def deleteMin(self):
        if self.is_empty():
            raise self.MyException("Heap is empty")
            return 0

        min_element = self.collection[0]
        self.collection[0] = None
        self.num_items -= 1
        self.helper_restore_heap_property_delete()

        return min_element

    def helper_restore_heap_property_delete(self, idx = 0):
        if idx + 1 < self.size:
            smallest = idx + 1
        else:
            smallest = idx

        idx_left_child = (idx * 2)+ 1
        idx_right_child = (idx * 2) + 2

        if idx_left_child < self.num_items and self.collection[idx_left_child] < self.collection[smallest]:
            smallest = idx_left_child

        if idx_right_child < self.num_items and self.collection[idx_right_child] < self.collection[smallest]:
            smallest = idx_left_child

        if smallest != idx:
            temp = self.collection[idx]
            self.collection[idx] = self.collection[smallest]
            self.collection[smallest] = temp

            self.helper_restore_heap_property_delete(smallest)


    def collection_size(self): # returns the number of elements; num_items
        return self.num_items
