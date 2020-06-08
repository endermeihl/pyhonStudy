def bin_search(items, key):
    """二分法查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if items[mid] == key:
            return mid
        elif items[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1
