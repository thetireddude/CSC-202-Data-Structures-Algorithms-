import graph
import find_shortest_path_4 as S

g2 = graph.Graph()

for i in range(1, 8):
    g2.addVertex(i)

g2.addEdge(1, 2, 2)
g2.addEdge(1, 4, 1)
g2.addEdge(2, 4, 3)
g2.addEdge(2, 5, 10)
g2.addEdge(3, 1, 4)
g2.addEdge(3, 6, 5)
g2.addEdge(4, 3, 2)
g2.addEdge(4, 5, 2)
g2.addEdge(4, 6, 8)
g2.addEdge(4, 7, 4)
g2.addEdge(5, 7, 6)
g2.addEdge(7, 6, 1)

S.shortest_path(g2.vertList[1], g2)



