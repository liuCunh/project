def func(list1, m):
    nums = len(list1)
    for i in range(0, nums):
        for j in range(i, nums):
            if list1[i] + list1[j] == m:
                return list1[i], list1[j]


if __name__ == '__main__':
    n = list(map(int, input().split()))  # 输入的n个数
    m = int(input())  # 输入的m
    print(func(n, m))

