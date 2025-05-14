import unittest
import graph
from find_shortest_path_3 import shortest_path

class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected_output = "vertex: 0, distance: 0, prev. vertex: 0\nvertex: 1, distance: 5, prev. vertex: 0\nvertex: 2, distance: 9, prev. vertex: 1\nvertex: 3, distance: 18, prev. vertex: 2\nvertex: 4, distance: 10, prev. vertex: 5\nvertex: 5, distance: 2, prev. vertex: 0\n"

        g = graph.Graph()
        for i in range(6):
            g.addVertex(i)

        # print(g.vertList)

        g.addEdge(0, 1, 5)
        g.addEdge(0, 5, 2)
        g.addEdge(1, 2, 4)
        g.addEdge(2, 3, 9)
        g.addEdge(3, 4, 7)
        g.addEdge(3, 5, 3)
        g.addEdge(4, 0, 1)
        g.addEdge(5, 4, 8)
        g.addEdge(5, 2, 1)

        output = shortest_path(g.vertList[0], g)
        self.assertEqual(expected_output, output)  # add assertion here

if __name__ == '__main__':
    unittest.main()
