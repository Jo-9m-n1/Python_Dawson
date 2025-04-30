def binarySearch(lst, target):
    low = 0
    high = len(lst) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elem = 5
result = binarySearch(lst, elem)
if result != -1:
    print(f"Element {elem} found at index {result}.")
else:
    print(f"Element {elem} not found in the list.")