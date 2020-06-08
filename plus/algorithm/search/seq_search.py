def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if key == items:
            return index
    return -1

