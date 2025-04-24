import numpy as np
import matplotlib

# a = np.array([[0, 1], [2, 3], [4, 5]], dtype=complex)
# print(a)

# # 显示数组维度
# print(a.shape)

# a = np.array([[0, 1], [2, 3], [4, 5]], dtype=np.int8)
# # 显示字节大小
# print(a.itemsize)
#
#
# s = np.arange(10)
# print(s)

# # 字符串切片 slice(start, end, step)
# s1 = slice(1, 9, 2)
# print(s[s1])

a = np.array([[0, 1], [1, 2]])
b = np.array([[3, 4], [5, 6]])

# 点积
print(np.dot(a, b))
print(a + b)

import numpy as np

a = np.array([[0, 1], [1, 2]])
b = np.array([[3, 4], [5, 6]])
print(a, b, "\n")

print(a+b)
print(a-b)
print(a*b)
print(a/b, "\n")

# 距离
s = np.arange(10)
print(s)
s1 = slice(1, 9, 2)
print(s[s1], "\n")

# 形状
res = np.sqrt(np.sum(np.square(b-a)))
print(res, "\n")

# 点积
print(np.dot(a, b))
print(a + b)

