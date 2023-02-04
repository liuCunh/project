# 内部函数
"""
内部寒素特点
1、可以访问外部函数的变量
2、内部函数可以修改外部函数的可变类型的变量
3、内部函数调用函数内不可变参数时，需要加nonlocal
   内部函数修改全局的不可变的变量时，需要加global
4、locals()查看本地变量有哪些，返回一个字典
   globals()查看全局变量有哪些，以字典形式返回
"""


def func():
    s = 100
    list1 = [1, 2, 4, 3]

    # 声明内部函数
    def inner_func():
        nonlocal s
        # list1 中每项加5
        for i, val in enumerate(list1):
            list1[i] = val + s

        list1.sort()
        s += 1

    inner_func()

    # locals()内置函数查看，可以看到当前函数中声明的变量有哪些
    # locals() 以key：value类型返回
    print(locals())
    print(globals())


func()
