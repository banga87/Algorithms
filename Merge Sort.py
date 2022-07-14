def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_idx = len(items) // 2
    left_idx = items[:middle_idx]
    right_idx = items[middle_idx:]

    left_sorted = merge_sort(left_idx)
    right_sorted = merge_sort(right_idx)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
        
    if left:
        result += left
    
    if right:
        result += right

    return result

unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]

ordered_list1 = merge_sort(unordered_list1)

print(ordered_list1)
