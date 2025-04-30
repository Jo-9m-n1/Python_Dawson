def binarySearch(lst, low, high, target):
    if high >= low:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            return binarySearch(lst, low, mid - 1, target)
        else:
            return binarySearch(lst, mid + 1, high, target)
    else:
        return -1
    
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elem = 5
result = binarySearch(lst, 0, len(lst) - 1, elem)
if result != -1:
    print(f"Element {elem} found at index {result}.")
else:
    print(f"Element {elem} not found in the list.")