def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = array[temp]

def bubble_swap(array):
    for element in range(len(array) - 1):
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                # swap(array, index, index + 1)
                array[index], array[index + 1] = array[index + 1], array[index]
    return array

unsorted = [5, 2, 9, 1, 5, 6]
print(range(len(unsorted) - 1))
sorted = bubble_swap(unsorted)

print(sorted)