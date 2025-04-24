# 匿名函数：简化函数定义
"""
格式：
    lambde 参数一，参数二... : 运算
"""

# def func():
#     print('aas')
#
#
# def add(a, b):
#     s = a + b
#     return s
x = lambda a, b: a + b

print(x)

x(1, 2)

def func1(a, b, func_my):
    print(a, b)
    return func_my(a, b)


print(func1(1, 2, lambda a, b: a + b))
