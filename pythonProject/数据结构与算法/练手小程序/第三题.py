"""
给定一个列表和一个整数，设计算法找到两个数的下标，使得两个数之和为给定的整数。保证肯定仅有一个结果。
    例如，列表[1, 2, 5, 4]于目标整数3， 1+2=3，结果为(0, 1)
"""


def s(num, target):
    pass
    # 自己写的
    # num.sort()
    # for i in range(len(num)):
    #     if num[i] <= target:
    #         for j in range(1, len(num)):
    #             if num[j] <= target:
    #                 count = num[i]+num[j]
    #                 if count == target:
    #                     print(i, j)
    #             else:
    #                 break

    # 方法二：
    # n = len(num)
    # for i in range(n):
    #     for j in range(i):
    #         if num[i] + num[j] == target:
    #             return sorted([i, j])

# 方法三:假设列表有序


class Solutino:
    def binary_search(self, li, left, right, val):
        while left <= right:
            mid = (left + right) // 2
            if li[mid] == val:
                return mid
            elif li[mid] > val:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return None

    def twoSum(self, nums, target):
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b >= a:
                j = self.binary_search(nums, i+1, len(nums)-1, b)
            else:
                j = self.binary_search(nums, 0, i-1, b)
            if j:
                break
            return sorted([i+1, j+1])


# 方法四：
class Solutino1(object):
    def binary_search(self, li, left, right, val):
        while left <= right:
            mid = (left + right) // 2
            if li[mid][0] == val:
                return mid
            elif li[mid][0] > val:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return None

    def twoSum(self, nums, target):
        new_nums = [[num, i] for i, num in enumerate(nums)]
        new_nums.sort(key=lambda x: x[0])  # 对二位列表中nums的值进行排序
        for i in range(len(new_nums)):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                j = self.binary_search(new_nums, i+1, len(new_nums)-1, b)
            else:
                j = self.binary_search(new_nums, 0, i-1, b)
            if j:
                break
            return sorted([new_nums[i][i], new_nums[i][j]])





