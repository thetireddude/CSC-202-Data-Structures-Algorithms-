# insertion sort --> pick an index, compare element at that index to every element to the left of it
#                     If the element on the left is larger, next compare with the element on its left
#                     keep comparing till the element on the left is not larger
#                     in the end swap original element at index with the left most element you compared with
from crypt import methods

# selection sort --> define a start_index
#                     set element at (start_index - 1) as the smallest
#                     iterate through the array and compare each element to smallest
#                     if they are smaller, make that element "smallest"
#                     swap the element at start_index with smallest element
#                     increase start_index by one

# quick sort --> choose a pivot element
#                 this can be the first element, random or calculated using median-of-three method
#                 make separate sublists that store elements smaller/larger than the pivot
#                 recursively call quick sort on these sublists until the no. of elements in them is one or two,
#                   then sort the sublists
#                 append in order - smaller, equal, larger to a new list and return that in each recursive call
