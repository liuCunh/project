# map()函数
list1 = [1, 2, 3, 4, 4, 5, 6]
li = list1
print(list1)

# res = map(lambda x: x + 1, list1)
# print(list(res))

func = lambda x: x if x % 2 == 0 else x + 1
res = map(func, list1)
print(list(res))

# 上下等价
# for index, i in enumerate(li):
#     if not i % 2 == 0:
#         list1[index] = i + 1
# print(li)


# reduce(): 对列表中的函数进行数学运算

from functools import reduce

tuple1 = (2, 3, 4, 5, 6)

res = reduce(lambda x, y: x+y, tuple1)  # 对元组中的元素叠加
print(res)

tupel12 = (1,)
res = reduce(lambda x, y: x-y, tupel12, 10)
print(res)