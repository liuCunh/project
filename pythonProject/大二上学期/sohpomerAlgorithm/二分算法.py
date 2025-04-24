def func(list1, m):
    list1.sort()
    for i in range(len(list1)-1):
        res = m - list1[i]

        # 二分查找
        left, right = i + 1, len(list1)-1
        while left <= right:
            mid = (left + right) // 2
            if list1[mid] == res:
                return list1[i], list1[mid]
            elif list1[mid] < res:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == '__main__':
    n = list(map(int, input().split()))  # 输入的n个数
    m = int(input())  # 输入的m
    x, y = func(n, m)
    print(x, y)
