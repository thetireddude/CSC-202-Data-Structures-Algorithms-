class MyHashTable:

    def __init__(self, table_size = 11):
        self.table_size = table_size
        self.hash_table = [[] for x in range(table_size)]
        self.num_items = 0
        self.num_collisions = 0

    def hash_function(self, key):
        return key % self.table_size

    def insert(self, key, item):
        if not(key >= 0):
            raise ValueError("Key must be a positive integer")
        pair = (key, item)
        hash_value = self.hash_function(key)

        self.helper_insert(pair, hash_value)
        self.num_items += 1

        load_factor = self.load_factor()

        if load_factor > 1.5:
            self.rehash()

    def helper_insert(self, pair, hash_value):
        for idx, element in enumerate(self.hash_table[hash_value]):
            if pair[0] == element[0]:
                self.hash_table[hash_value][idx] = pair
                return

        print(len(self.hash_table[hash_value]))
        if len(self.hash_table[hash_value]) > 0:   # checks if bucket is not empty
            self.num_collisions += 1
        self.hash_table[hash_value].append(pair)

    def rehash(self):
        new_size = (2 * self.table_size) + 1
        self.table_size = new_size

        temp = self.hash_table
        self.hash_table = [[] for x in range(new_size)]
        self.num_items = 0
        self.num_collisions = 0

        for bucket in temp:
            for pair in bucket:
                self.insert(pair[0], pair[1])

    def get(self, key):
        for bucket in self.hash_table:
            for pair in bucket:
                if pair[0] == key:
                    return pair
        raise LookupError("Key not found")

    def remove(self, key):
        for bucket in self.hash_table:
            for idx, pair in enumerate(bucket):
                if pair[0] == key:
                    self.num_items -= 1
                    return bucket.pop(idx)

    def size(self):
        return self.num_items

    def load_factor(self):
        return round((self.num_items / self.table_size), 1)

    def collisions(self):
        return self.num_collisions