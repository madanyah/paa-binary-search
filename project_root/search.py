def BinarySearch(list, value):
    left, right = 0, len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == value:
            return mid
        elif value < list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1