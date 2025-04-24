# 闭包: 将内部函数通过return返回(别加括号，加货号就成调用了)
# 在函数中提出的概念
"""
1、在外雇函数中定义了内部函数
2、外部函数有返回值且返回值为内部函数名(不加括号)
3、内部函数引用外部函数的变量

格式：
def 外部函数():
    ...
    def 内部函数():
        ...
    return 内部函数名

闭包作用：
    1、保存返回闭包时的状态(外层函数变量


"""


# def func():
#     a = 100
#
#     def inner_func():
#         b = 99
#         print(a, b)
#
#     print(locals())
#     return inner_func
#
#
# x = func()
# x()
# print(x)


# 闭包函数
def func(a, b):
    c = 10

    def inner_func():
        num = a + b + c
        print(f'相加后的结果为={num}')

    return inner_func


# ifunc = func(1, 2)
# 装饰器 = func(2, 8)
# ifunc()
# 装饰器()

# 闭包应用
