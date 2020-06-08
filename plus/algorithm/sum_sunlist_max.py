def main():
    items = list(map(int, input().split()))
    size = len(items)
    max_result = items[0]
    max_temp = items[0]
    max_temp2 = items[0]
    for i in range(1, size - 1):
        max_temp = max(0, max_temp + items[i])
        max_result = max(max_temp, max_result)
    return max_result


if __name__ == '__main__':
    print(main())
