from graph import g as g1
from queue_linked_list import QueueLinkedList as Queue

def shortest_path(vertex, graph):

    path_list, index_map = path_list_maker(graph, vertex)
    visited_list = [False] * len(path_list)
    # print(path_list)
    q1 = Queue()
    curr_vert = vertex

    q1.enqueue(curr_vert)
    while check_visited(path_list):
        curr_vert = q1.peek()
        curr_vert_idx = index_map[curr_vert]

        path_list[curr_vert_idx][0].visited = True
        visited_list[curr_vert_idx] = True

        for connected_vert in curr_vert.connectedTo:
            # print(path_list)
            if connected_vert.key != vertex.key:
                q1.enqueue(connected_vert)

                connected_vert_idx = index_map[connected_vert]

                parent_idx = curr_vert_idx
                total_distance = curr_vert.connectedTo[connected_vert]

                a = path_list[parent_idx][2]

                while path_list[parent_idx][2] is not None and path_list[parent_idx][2] != 0:
                    prev_idx = parent_idx
                    parent_idx = index_map[path_list[prev_idx][2]]
                    new_parent_to_prev_distance = path_list[parent_idx][0].connectedTo[path_list[prev_idx][0]]
                    total_distance += new_parent_to_prev_distance

                if  path_list[connected_vert_idx][1] is None or total_distance < path_list[connected_vert_idx][1]:
                    path_list[connected_vert_idx][1] = total_distance
                    path_list[connected_vert_idx][2] = curr_vert
        q1.dequeue()

    output = ""
    for element in path_list:

        output += f"vertex: {element[0]}, distance: {element[1]}, prev. vertex: {element[2]}\n"
    print(output)
    return output
    # print(path_list)

def queue_find(key, queue1):    # returns true if key is NOT already in the queue
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


# shortest_path(g1.vertList[0], g1)