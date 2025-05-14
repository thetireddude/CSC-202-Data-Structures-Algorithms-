import unittest
from sep_chain_ht import MyHashTable

class MyTestCase(unittest.TestCase):
    def test_hash_table_creation(self):
        h1 = MyHashTable()
        self.assertEqual(h1.table_size, 11)

    def test_insert(self):
        h1 = MyHashTable()

        h1.insert(45, "test")
        h1.insert(23, "test")
        h1.insert(21, "test")

        self.assertEqual(h1.num_items, 3)

    def test_insert_same_key(self):
        h1 = MyHashTable()

        h1.insert(12, "apples")
        self.assertEqual(h1.hash_table[h1.hash_function(12)][0], (12, "apples"))

        h1.insert(12, "pancakes")
        self.assertEqual(h1.hash_table[h1.hash_function(12)][0], (12, "pancakes"))

    def test_rehash(self):
        h1 = MyHashTable(3)

        self.assertEqual(h1.table_size, 3)

        h1.insert(12, "kimbap")
        h1.insert(13, "pocky")
        h1.insert(15, "mochi")
        h1.insert(20, "dango")
        h1.insert(25, "taiyaki")

        self.assertEqual(h1.table_size, 7)

    def test_get(self):
        h1 = MyHashTable()

        h1.insert(12, "tokyo")
        h1.insert(13, "kyoto")
        h1.insert(15, "osaka")
        h1.insert(20, "kanto")
        h1.insert(25, "hokkaido")

        self.assertEqual(h1.get(13), (13, "kyoto"))

    def test_get_exception_handling(self):
        h1 = MyHashTable()

        with self.assertRaises(LookupError) as e:
            h1.get(12)
        self.assertEqual(str(e.exception), "Key not found")

    def test_remove(self):
        h1 = MyHashTable()

        h1.insert(12, "nissan")
        h1.insert(13, "honda")
        h1.insert(15, "toyota")
        h1.insert(20, "mitsubishi")
        h1.insert(25, "suzuki")

        self.assertEqual(h1.remove(20), (20, "mitsubishi"))
        self.assertEqual(h1.num_items, 4)

    def test_size(self):
        h1 = MyHashTable()

        h1.insert(12, "Supra")
        h1.insert(13, "GTR")
        h1.insert(15, "NSX")

        self.assertEqual(h1.size(), 3)

    def test_collisions(self):
        h1 = MyHashTable(5)

        h1.insert(12, "Honda")      # causes no collision
        h1.insert(22, "Hokkaido")   # causes collision bcz hash_value is the same
        h1.insert(5, "Mochi")       # causes no collision
        h1.insert(12, "Nissan")     # causes update bcz key is the same


        self.assertEqual(h1.collisions(), 1)

if __name__ == '__main__':
    unittest.main()
