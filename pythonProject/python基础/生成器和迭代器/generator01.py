"""
得到生成器方式
1、通过列表推导式得到生成器

"""

# [0, 3, 6, 9, 12, 15, 18, 21,...27]

# 得到列表推导式
newlist = [x*3 for x in range(10)]
print(type(newlist))  # list

# 得到生成器
g = (x*3 for x in range(10))
print(type(g))  # generator

# 方式一：通过调用__next__() 方式得到元素
print(g.__next__())
print(g.__next__())
print(g.__next__())

# 方式二：next(生成器对象)    builtine 系统内置函数
# 每次调用一次next元素，则会产生一个元素
print(next(g))
print(next(g))
print(next(g))