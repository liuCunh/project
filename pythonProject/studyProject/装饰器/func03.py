# 装饰器
# def func(number):
#     a = 100
#
#     def inner_func():
#         nonlocal a, number
#         number += 1
#         for i in range(number):
#             a += 1
#         print(f'修改后a={a}')
#
#     return inner_func


# a = 50
# f1 = func(5)
# print(f1)


# 地址引用

# def test():
#     print('----test----')
#
#
# t = test
#
#
# def func(f):
#     print(f)
#     f()
#     print('-----func:')
#
#
# func(test)

"""
特点：
1、函数A作为参数出现的(函数B就接收A作为参数)
2、要有闭包的特点
"""


# 装饰器
def decorate(func):
    a = 100
    print('wrapper外层打印测试')

    def wrapper():
        func()
        print('------装修')
        print('----摆家电')
        print(a)

    print('wrapper打印完成')
    return wrapper


# 装饰器的使用
@decorate
def house():
    print('我是毛坯房---')


"""
1、houres被装饰函数
2、被装饰函数作为参数传递给decorate
3、执行装饰器函数
4、
"""
print(house)
