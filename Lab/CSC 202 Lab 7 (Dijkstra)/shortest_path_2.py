from graph import g as g1
from queue_linked_list import QueueLinkedList as Queue

def shortest_path(vertex, graph):

    path_list, index_map = path_list_maker(graph, vertex)
    visited_list = [False] * len(path_list)
    print(path_list)
    q1 = Queue()
    curr_vert = vertex

    q1.enqueue(curr_vert)
    while check_visited(path_list):
        curr_vert = q1.peek()
        curr_vert_idx = index_map[curr_vert]

        path_list[curr_vert_idx][0].visited = True
        visited_list[curr_vert_idx] = True

        for vert in curr_vert.connectedTo:
            if vert.key != vertex.key:
                value = queue_find(vert.key, q1)
                if value:
                    q1.enqueue(vert)

                    connected_vert_idx = index_map[vert]

                    idx = connected_vert_idx
                    total_distance = curr_vert.connectedTo[vert]

                    while path_list[idx][2] != 0 and path_list[idx][2] is not None:
                        idx = index_map[path_list[idx][2]]
                        total_distance += path_list[idx][1]

                    if  path_list[connected_vert_idx][1] is None or total_distance < path_list[connected_vert_idx][1]:
                        path_list[connected_vert_idx][1] = total_distance
                        path_list[idx][2] = curr_vert
        q1.dequeue()
    print(path_list)

def queue_find(key, queue1):    # returns true if key is not already in the queue
    if queue1.head is not None:
        curr = queue1.head
        while curr:
            curr_key = curr.item.key
            if curr_key == key:
                return False
            curr = curr.next
        return True
    return False


def check_visited(pathlist): # returns True if all vertexes have NOT been visited
    value = True
    for element in pathlist:
        if element[0].visited:
            value = False
        else:
            return True
    return value

def path_list_maker(graph, vertex):
    output = []
    index_map = {}
    for vert in graph.vertList:
        if graph.vertList[vert] == vertex:
            output.append([graph.vertList[vert], 0, 0])
        else:
            output.append([graph.vertList[vert], None, None])

    for idx, element in enumerate(output):
        index_map[element[0]] = idx
    # print(f"index map: {index_map}")
    return output, index_map


shortest_path(g1.vertList[0], g1)