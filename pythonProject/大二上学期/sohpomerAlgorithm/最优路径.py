import sys
sys.setrecursionlimit(100000)
def MaxSum(r, j):
    if r == n - 1:
        return matrix[r][j]
    sum1 = MaxSum(r + 1, j)
    sum2 = MaxSum(r + 1, j + 1)
    if sum1 > sum2:
        return sum1 + matrix[r][j]
    return sum2 + matrix[r][j]
n = int(input())
matrix = [0 for i in range(n)]
for i in range(n):
    temp = input().split()
    nums = map(int, temp)
    matrix[i] = list(nums)
MaxSum(0, 0)

def func(now, end):
    if now == n-1:
        return matrix[now][end]
    return max(func(now+1, end), func(now+1, end+1)) + matrix[now][end]


