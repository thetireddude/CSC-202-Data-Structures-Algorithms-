from graph import g as g1
from queue_linked_list import QueueLinkedList as Queue

dict1 = {"name": "Dude", "age": 34}
q1 = Queue()
curr_vert = g1.vertList[0]
# print(curr_vert)
#
# for vert in curr_vert.connectedTo:
#     print(f"vertex:{vert.key}, weight:{curr_vert.connectedTo[vert]}")

# q1.enqueue(curr_vert.connectedTo)
# print(q1.peek())

# for x in dict1:
#     print(x, dict1[x])

# q1.enqueue(curr_vert)
# print(q1)
# print(q1.head.item.connectedTo)

q1.enqueue(g1.vertList[0])
q1.enqueue(g1.vertList[1])
q1.enqueue(g1.vertList[5])
q1.enqueue(g1.vertList[2])
q1.enqueue(g1.vertList[4])

# def queue_find(key, queue1):
#     curr = queue1.head
#     while curr:
#         if curr.item.key == key:
#             return False
#         curr = curr.next
#     return True
#
# print(queue_find(2, q1))

curr_vert = g1.vertList[0]
for vert in curr_vert.connectedTo:
    print(curr_vert.connectedTo[vert])

