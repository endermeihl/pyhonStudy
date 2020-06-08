"""
动态规划 - 适用于有重叠子问题和最优子结构性质的问题
使用动态规划方法所耗时间往往远少于朴素解法(用空间换取时间)
"""


def fib(num, temp=None):
    if temp is None:
        temp = {}
    if num in (1, 2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 1)
        return temp[num]


if __name__ == '__main__':
    print(fib(5))
