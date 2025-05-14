import selection_sort
import insertion_sort
import quick_sort
import array_generator as rand_arr
import time

size = int(input("\nEnter size: "))
pivot_mode = input("\nEnter quick sort mode: ")
# random_array = rand_arr.random_array(size)
random_array = [1, 2, 3, 66, 6, 9, 13, 45, 78, 23, 43, 1, 2, 3, 66, 6, 9, 13, 45, 78, 23, 43]

unsorted_selection_sort = []
unsorted_insertion_sort = []
unsorted_quick_sort = []

unsorted_selection_sort.extend(random_array)
unsorted_insertion_sort.extend(random_array)
unsorted_quick_sort.extend(random_array)

print(f"\n selection sort")
# print(f"\nunsorted selection sort: {unsorted_selection_sort}")
selection_sort_start_time = time.time()
comparisons_selection_sort = selection_sort.selection_sort(unsorted_selection_sort)
selection_sort_end_time = time.time()
# print(f"sorted selection sort: {unsorted_selection_sort}")
print(f"number of comparisons: {comparisons_selection_sort}")
print(f"time taken: {(selection_sort_end_time - selection_sort_start_time) * 10000000}ms")

print(f"\n insertion sort")
# print(f"\nunsorted insertion sort: {unsorted_insertion_sort}")
insertion_sort_start_time = time.time()
comparisons_insertion_sort = insertion_sort.insertion_sort(unsorted_insertion_sort)
insertion_sort_end_time = time.time()
# print(f"sorted insertion sort: {unsorted_insertion_sort}")
print(f"number of comparisons: {comparisons_insertion_sort}")
print(f"time taken: {(insertion_sort_end_time - insertion_sort_start_time) * 10000000}ms")

print(f"\n quick sort")
# print(f"\nunsorted quick sort: {unsorted_quick_sort}")
quick_sort_start_time = time.time()
sorted_quick_sort, comparisons_quick_sort = quick_sort.quick_sort(unsorted_quick_sort, pivot_mode)
quick_sort_end_time = time.time()
print(f"sorted quick sort: {sorted_quick_sort}")
print(f"number of comparisons: {comparisons_quick_sort}")
print(f"time taken: {(quick_sort_end_time - quick_sort_start_time) * 10000000}ms")

