"""                                                             [
给定一个m*n的二维列表，查找一个数是否存在。列表有下列特征:                 [1, 3, 5, 7],
  * 每一行的列表从右到左已经排序好。                                   [10, 11, 16, 20],
  * 每一行第一个数比上一行最后一个数大                                 [23, 30, 34, 50]
                                                                ]
"""


def s(matrix, target=20):

    # 自己写的
    # for i in range(1, len(matrix)):
    #     result = matrix[i-1][1] <= target <= matrix[i][1]
    #     if result:
    #         left = 0
    #         right = len(matrix[i-1]) - 1
    #         while left <= right:
    #             mid = (left+right) // 2
    #             if matrix[i-1][mid] == target:
    #                 return i-1, mid
    #             elif matrix[i-1][mid] < target:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #         else:
    #             return None

    # 方法二
    # for line in matrix:
    #     if target in line:
    #         return True
    # return False

    # 方法三
    h = len(matrix)
    if h == 0:
        return False
    w = len(matrix[0])
    if w == 0:
        return False
    left = 0
    right = w * h - 1
    while left <= right:
        mid = (left+right) // 2
        i = mid // w
        j = mid % w
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return False


li = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
print(s(li))
