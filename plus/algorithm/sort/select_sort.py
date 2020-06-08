def select_sort(origin_items, comp=lambda x, y: x < y):
    """
    简单选择排序
    双循环，每次寻找之后元素中最小的放当当前循环的最前面
    """
    items = origin_items[:]
    length = len(items)
    for i in range(length - 1):
        temp_item = i
        for j in range(i + 1, length):
            if comp(items[j], items[temp_item]):
                temp_item = j
        items[i], items[temp_item] = items[temp_item], items[i]
    return items


if __name__ == '__main__':
    print(select_sort([3, 1, 4, 2, 5, 0, 9, 7, 8, 6]))
