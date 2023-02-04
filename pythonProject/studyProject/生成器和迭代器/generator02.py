# g = (x*3 for x in range(10))
#
# while True:
#     try:
#         t = next(g)
#         print(t)
#     except StopIteration:
#         print('没有更多的元素了')
#         break

# 定义生成器方式二： 借助函数完成
# 函数中出现一个yidld时，该函数就变成生成器了
"""
1、定义一个函数，函数中使用yield关键字
2、调用函数，接收调用的结果
3、得到的结果就是生成器
4、借助与next(), __next__() 得到元素

"""


def func():
    n = 0
    while True:
        n += 1
        yield n  # 出现这个关键字，就是一个生成器


g = func()


# print(next(g))
# print(next(g))
# print(next(g))

def fibnacci(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b  # 抛出b，且将程序在此停止
        a, b = b, a+b
        n += 1

    return "沒有更多的元素了"


f = fibnacci(8)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

