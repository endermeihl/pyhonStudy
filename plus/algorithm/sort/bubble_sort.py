def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = origin_items[:]
    length = len(items)
    for i in range(length - 1):
        swapped = False
        for j in range(i, length - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            for j in range(length - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


if __name__ == '__main__':
    print(bubble_sort([3, 1, 4, 2, 5, 0, 9, 7, 8, 6]))
