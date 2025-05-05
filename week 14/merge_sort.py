def mergeSort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2

    left_half = lst[:mid]
    right_half = lst[mid:]

    sorted_left = mergeSort(left_half)
    sorted_right = mergeSort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    pass