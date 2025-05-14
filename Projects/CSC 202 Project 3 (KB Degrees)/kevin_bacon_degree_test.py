import unittest
import find_shortest_path_3 as S
import kevin_bacon_degree as KBd

class MyTestCase(unittest.TestCase):
    def test_bacon_degree(self):
        expected_output = "Kevin Bacon, Donald Sutherland, Nicole Kidman, "
        output = KBd.bacon_degree(KBd.g, 'Nicole Kidman')
        self.assertEqual(expected_output,  output)

    def test_highest_bacon(self):
        expected_output = "Grace Kelly, 3"
        output = KBd.highest_bacon(KBd.g)
        self.assertEqual(expected_output,  output)

    def test_any_actors_bacon(self):
        expected_output = "Nicole Kidman, Donald Sutherland, Kevin Bacon, Tom Hanks, "
        output = KBd.any_actors_degree(KBd.g, 'Nicole Kidman', 'Tom Hanks')
        self.assertEqual(expected_output,  output)

    def test_bacon_actors_with_degree(self):
        expected_output = "Paul Herbert, Yves Aubert, Shane Zaza, Seretta Wilson, Lloyd Bridges, Nicole Kidman, Patrick Allen, Vernon Dobtcheff, Kate Winslet, "
        output = KBd.bacon_actors_with_degree(KBd.g, 2)
        self.assertEqual(expected_output,  output)

if __name__ == '__main__':
    unittest.main()
