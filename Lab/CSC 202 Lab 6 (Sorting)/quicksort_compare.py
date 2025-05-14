import quick_sort
import array_generator as rand_arr
import time

size = int(input("\nEnter size: "))
random_array = rand_arr.random_array(size)

unsorted_quick_sort_first = []
unsorted_quick_sort_mo3 = []

unsorted_quick_sort_first.extend(random_array)
unsorted_quick_sort_mo3.extend(random_array)


print(f"\n quick sort (pivot - first")
# print(f"\nunsorted quick sort: {unsorted_quick_sort}")
quick_sort_first_start_time = time.time()
sorted_quick_sort_first, comparisons_quick_sort_first = quick_sort.quick_sort(unsorted_quick_sort_first, "first")
quick_sort_first_end_time = time.time()
# print(f"sorted quick sort: {sorted_quick_sort}")
print(f"number of comparisons: {comparisons_quick_sort_first}")
print(f"time taken: {(quick_sort_first_end_time - quick_sort_first_start_time) * 10000000}ms")

print(f"\n quick sort (pivot - mo3")
# print(f"\nunsorted quick sort: {unsorted_quick_sort}")
quick_sort_mo3_start_time = time.time()
sorted_quick_sort_mo3, comparisons_quick_sort_mo3 = quick_sort.quick_sort(unsorted_quick_sort_mo3, "first")
quick_sort_mo3_end_time = time.time()
# print(f"sorted quick sort: {sorted_quick_sort}")
print(f"number of comparisons: {comparisons_quick_sort_mo3}")
print(f"time taken: {(quick_sort_mo3_end_time - quick_sort_mo3_start_time) * 10000000}ms")