# 递归函数
"""
普通函数 def fun(): pass
匿名函数 lambda 参数：返回结果
递归函数：普通函数的一种形式标表现

特点：
1、
"""


# 求列表的累加和
def sum(n):  # 1~n
    if n == 0:
        return 0
    return n + sum(n - 1)


print(sum(10))


# s = 0
# for i in range(11):
#     s += i
#
# print(s)
def recursion(n):
    if n == 0:
        return 0
    recursion(n-1)
    print(f'--->{n}')


recursion(5)
