import numpy as np

# x = np.arange(9)
# res = np.split(x, 3)  # 等距切成3个数组
# x1 = x.tolist()  # 转换成列表
# print(x1)
#
# arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# print(np.mean(arr))  # 算数平均数
#
# s1 = np.array([1, 2, 3, 4, 1, 2, 4])
# s1_a = np.unique(s1)  # 数组去重
# print(s1_a)

# 数组合并
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[10, 20, 30], [40, 50, 60]])
res1 = np.vstack((a, b))  # 纵轴链接
res2 = np.hstack((a, b))  # 横轴链接
print(res1, "\n")
print(res2)

# 数据统计
a = np.array([[10, 2, 30], [12, 15, 45], [34, 78, 91]])
print(np.median(a))  # 中值
print(np.mean(a))  # 算数平均数
print(np.std(a))  # 标准差
print(np.var(a))  # 方差

# 排序
s = np.array([1, 2, 4, 6, 7, 8, 9, 5, 12, 14, 54, 34, 67, 99, 101])
print(np.sort(s))  # 给数组排序
print(np.argsort(s))  # 返回从小到大的索引
a = np.array([[1, 3, 2], [5, 4, 6], [7, 9, 8]])
print(np.sort(a, axis=1))  # 行排序
print(np.sort(a, axis=0))  # 列排序

# 判断空值
print(np.isnan(3))
print(np.isnan(0))
a = float("nan")
print(np.isnan(a))

print(np.extract(s > 30, s))  # 筛选数据，将s中大于30的值筛选出来

s1 = np.array([1, 2, 3, 4, 1, 2, 3])
print(np.unique(s1))  # 去重，将宠重复数据只保留一次

print(np.amax(s))  # 返回最大值
print(np.amin(s))  # 返回最小值

