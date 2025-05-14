import graph as graphs
import find_shortest_path_3 as S

# Code to build the example graph:
# Note that the addBiEdge function adds two edges to account for undirected edges.
# add this function to your graph class:

g = graphs.Graph()
g.addVertex('Kevin Bacon')
g.addVertex('Tom Hanks')
g.addVertex('Bill Paxton')
g.addVertex('Paul Herbert')
g.addVertex('Yves Aubert')
g.addVertex('Shane Zaza')
g.addVertex('Seretta Wilson')
g.addVertex('Meryl Streep')
g.addVertex('John Beluci')
g.addVertex('Kathleen Quinlan')
g.addVertex('Donald Sutherland')
g.addVertex('Lloyd Bridges')
g.addVertex('Grace Kelly')
g.addVertex('Nicole Kidman')
g.addVertex('Patrick Allen')
g.addVertex('Glenn Close')
g.addVertex('John Gielgud')
g.addVertex('Vernon Dobtcheff')
g.addVertex('Kate Winslet')

g.addBiEdge('Kevin Bacon', 'Tom Hanks')
g.addBiEdge('Kevin Bacon', 'John Beluci')
g.addBiEdge('Kevin Bacon', 'Meryl Streep')
g.addBiEdge('Kevin Bacon', 'Donald Sutherland')
g.addBiEdge('Kevin Bacon', 'Bill Paxton')
g.addBiEdge('Kevin Bacon', 'Kathleen Quinlan')
g.addBiEdge('Tom Hanks', 'Kathleen Quinlan')
g.addBiEdge('Tom Hanks', 'Bill Paxton')
g.addBiEdge('Tom Hanks', 'Paul Herbert')
g.addBiEdge('Tom Hanks', 'Yves Aubert')
g.addBiEdge('Tom Hanks', 'Shane Zaza')
g.addBiEdge('Tom Hanks', 'Seretta Wilson')
g.addBiEdge('Tom Hanks', 'Lloyd Bridges')
g.addBiEdge('Lloyd Bridges', 'Grace Kelly')
g.addBiEdge('Donald Sutherland', 'Patrick Allen')
g.addBiEdge('Donald Sutherland', 'Nicole Kidman')
g.addBiEdge('Donald Sutherland', 'Vernon Dobtcheff')
g.addBiEdge('Nicole Kidman', 'Glenn Close')
g.addBiEdge('Nicole Kidman', 'John Gielgud')
g.addBiEdge('Bill Paxton', 'Kate Winslet')
g.addBiEdge('Patrick Allen', 'John Gielgud')
g.addBiEdge('Nicole Kidman', 'John Gielgud')
g.addBiEdge('Vernon Dobtcheff', 'John Gielgud')

def bacon_degree(g, actor):
# Takes an actor name and returns the shortest path to Kevin Bacon
    output_1 = S.shortest_path(g.vertList['Kevin Bacon'], g)

    actor_idx = search_output(actor, output_1)

    path = output_1[actor_idx][0].key + ", "

    while output_1[actor_idx][2] != 0:
        actor_idx = search_output(output_1[actor_idx][2].key, output_1)
        path = output_1[actor_idx][0].key + ", " + path
    return path

def search_output(actor, output):   # returns the index in the output of the actor we are looking for
    for idx, element in enumerate(output):
        if element[0].key == actor:
            return idx

def bacon_actors_with_degree(g, n):
# Returns all actors with degree n to Kevin Bacon
    output_4 = S.shortest_path(g.vertList['Kevin Bacon'], g)
    result = ""
    for element in output_4:
        if element[1] == n:
            result += element[0].key + ", "
    return result

def highest_bacon(g):
# Returns the actor(s) with the highest Bacon degree
    output_2 = S.shortest_path(g.vertList['Kevin Bacon'], g)

    highest_degree = 0
    for element in output_2:
        if element[1] > highest_degree:
            highest_degree = element[1]
            actor = element[0].key
    result = str(actor) + ", " + str(highest_degree)
    return result

def any_actors_degree(g, actor1, actor2):
# A more general function to return the path length between any two actors
    output_3 = S.shortest_path(g.vertList[actor1], g)

    actor_idx = search_output(actor2, output_3)

    path = output_3[actor_idx][0].key + ", "

    while output_3[actor_idx][2] != 0:
        actor_idx = search_output(output_3[actor_idx][2].key, output_3)
        path = output_3[actor_idx][0].key + ", " + path
    return path