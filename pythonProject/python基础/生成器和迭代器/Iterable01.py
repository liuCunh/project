# 可迭代对象 1.生成器， 2.元组 列表 集合 字典 字符串
# 如何判断一个对象是否可迭代 isinstance()
from collections.abc import Iterable

list1 = [1, 2, 4, 5]
print(isinstance(list1, Iterable))

f = isinstance('abc', Iterable)
print(f)

f = isinstance(100, Iterable)
print(f)
g = (x + 1 for x in range(10))
f = isinstance(g, Iterable)
print(f)


"""
迭代器： 可以被next()函数调用并不断返回下一个值的对象被称为迭代器

可迭代的 是不是就是 迭代器？————》看是否能用next() 函数调用

生成器是可迭代的，也是迭代器
list是可迭代的的，但不是迭代器

list --> iter() --> 迭代器  通过iter()函数将可迭代的元素变成一个迭代器
"""
list1 = [1,2,3,4,5]
list1 = iter(list1)
print(next(list1))
print(next(list1))
print(next(list1))
"""
生成器与迭代器：
 

"""