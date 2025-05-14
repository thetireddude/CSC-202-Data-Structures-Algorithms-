import array_generator as rand_arr
import time

def insertion_sort(alist):
    num_comparisons = 0
    for x in range(1, len(alist)):
        key = alist[x]
        index = x
        while index > 0 and key < alist[index - 1]:
            num_comparisons += 1
            alist[index] = alist[index - 1]
            index -= 1
        alist[index] = key
    return num_comparisons

# blah = rand_arr.random_array(1000)
# print(f"unsorted array: {blah}")
# start_time = time.time()
# qwerty = insertion_sort(blah)
# end_time = time.time()
# print(f"sorted array: {blah}")
# print(f"number of comparisons: {qwerty}")
# print(f"time taken: {(end_time - start_time) * 10000000}ms")


