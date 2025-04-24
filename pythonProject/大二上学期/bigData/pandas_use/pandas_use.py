import pandas as pd
import numpy as np

# s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# print(s)
#
# # 单个键值
# print(s['a'])
#
# # 多个键值
# print(s[['b', 'd']])
#
# # 条件筛选
# print(s[s > 30])
# print(s[s < 20])
# print(s[s == 30])
#
# # 算数运算
# print(s + 3)
# print(s - 3)
# print(s * 3)
# print(s / 3)
#
# # 条件运算
# print('b' in s)
#
# s1 = pd.Series([1, 2, 3, 4])
# s2 = pd.Series([10, 20, 30])
# res1 = s1 * s2
# res2 = s2 / s1
# res3 = s1 + s2
# res4 = s2 - s1

s = pd.Series([1, 2, 3, np.nan, 5, 6])

d1 = pd.Series(np.random.rand(10))  # [0, 1]范围
d2 = pd.Series(np.random.randn(10))  # (-1, 0]范围

print(d1)
print(d2)
