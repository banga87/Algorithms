# Quick Sort splits an array or list around a "pivot element"
# This element is compared against each element in the list
# < and > operators are used to determine greater than or lesser than placement
# Recursive calls continue to split the array into smaller chunks until the base case is reached

from random import randrange

def quicksort(list, start, end):
    # Base case
    if start >= end:
        return list

    # Pivot index and element
    pivot_idx = randrange(start, end)
    pivot_element = list[pivot_idx]

    # Swap pivot element with last element in list
    list[pivot_idx], list[end] = list[end], list[pivot_idx]

    # Create lesser than pointer
    lesser_than_pointer = start

    # Loop through and swap lesser than values + increment pointer += 1
    for i in range(start, end):
        if list[i] < pivot_element:
            list[i], list[lesser_than_pointer] = list[lesser_than_pointer], list[i]
            lesser_than_pointer += 1

    # Swap pointer element with end element
    list[lesser_than_pointer], list[end] = list[end], list[lesser_than_pointer]

    # Recursive calls to lesser than partition + greater than partition
    quicksort(list, start, lesser_than_pointer - 1)
    quicksort(list, lesser_than_pointer + 1, end)

# unsorted_list = [7, 24, 36, 12, 42, 3]
# print(unsorted_list)
# quicksort(unsorted_list, 0, len(unsorted_list) - 1)
# print(unsorted_list)

    