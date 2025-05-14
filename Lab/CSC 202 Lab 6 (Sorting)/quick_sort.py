import time
import array_generator as rand_arr

def quick_sort(alist, n_comparisons, pivot_mode = "mo3"):
    num_comparisons = n_comparisons
    smaller_elements = []
    equal_elements = []
    larger_elements = []
    all_elements = []

    sorted_smaller = []
    sorted_larger = []

    if pivot_mode == "first":
        pivot = alist[0]
    elif pivot_mode == "mo3":
        pivot = find_pivot(alist)

    for element in alist:
        num_comparisons += 1
        if element < pivot:
            smaller_elements.append(element)
        elif element > pivot:
            larger_elements.append(element)
        else:
            equal_elements.append(element)

    if len(smaller_elements) > 2:
        sorted_smaller, num_comparisons = quick_sort(smaller_elements, num_comparisons, pivot_mode)
    else:
        if len(smaller_elements) == 2:
            if smaller_elements[0] > smaller_elements[1]:
                sorted_smaller.append(smaller_elements[1])
                sorted_smaller.append(smaller_elements[0])
            else:
                sorted_smaller.extend(smaller_elements)
        elif len(smaller_elements) == 1:
            sorted_smaller.extend(smaller_elements)

    if len(larger_elements) > 2:
        sorted_larger, num_comparisons = quick_sort(larger_elements, num_comparisons, pivot_mode)
    else:
        if len(larger_elements) == 2:
            if larger_elements[0] > larger_elements[1]:
                sorted_larger.append(larger_elements[1])
                sorted_larger.append(larger_elements[0])
            else:
                sorted_larger.extend(larger_elements)
        elif len(larger_elements) == 1:
            sorted_larger.extend(larger_elements)

    all_elements.extend(sorted_smaller)
    all_elements.extend(equal_elements)
    all_elements.extend(sorted_larger)

    return all_elements, num_comparisons

def find_pivot(alist):
    median_three = []
    median_three.extend([alist[0], alist[len(alist) // 2], alist[-1]])

    smallest = median_three[0]
    idx = 0
    for i in range(len(median_three)):
        if median_three[i] < smallest:
            smallest = median_three[i]
            idx = i
    median_three.pop(idx)
    if median_three[0] < median_three[1]:
        return median_three[0]
    else:
        return median_three[1]


blah3= rand_arr.random_array(100)
print(f"unsorted: {blah3}")
start_time = time.time()
blah4, comparisons = quick_sort(blah3, 0)
end_time = time.time()
print(f"sorted: {blah4}")
print(f"comparisons: {comparisons}")
print(f"time taken: {(end_time - start_time) * 1000000}ms")


