import array_generator
import time

def selection_sort(alist):
    length = len(alist)
    start_idx = 1
    num_comparisons = 0

    while start_idx < length:
        smallest = alist[start_idx - 1]
        idx = None
        for i in range(start_idx, length):
            num_comparisons += 1
            if alist[i] < smallest:
                smallest = alist[i]
                idx = i
        if idx:
            alist[idx] = alist[start_idx - 1]
            alist[start_idx - 1] = smallest
        start_idx += 1
    return num_comparisons


# blah2 = rand_arr.random_array(200)
# print(f"unsorted array: {blah2}")
# start_time = time.time()
# comparisons = selection_sort(blah2)
# end_time = time.time()
# print(f"sorted array: {blah2}")
# print(f"number of comparisons: {comparisons}")
# print(f"time taken: {(end_time - start_time) * 1000000}ms")