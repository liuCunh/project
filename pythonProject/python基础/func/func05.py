# global
# 局部变量 全局变量
# 声明在函数外层的是全局变量，所以函数都可以访问
name = 'guagua'


def func():
    # 函数内部声明的变量，局部变量仅限于在函数内部使用
    s = 'abcd'
    s += 'X'
    print(s, name)


def func1():
    global name  # 调用全局变量时不用global关键字，修改这需要global关键字
    name += '是个干饭人！'
    print(name)


def func2():
    name = '唐淼'
    print(name)


func2()
func1()
