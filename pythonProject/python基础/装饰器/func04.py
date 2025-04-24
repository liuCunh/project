# 登录校验
import time


def decorate(func):
    def wrapper(*args, **kwargs):
        print(f'*arge={args}, **kwargs={kwargs}')
        print('正在进行校验....')
        time.sleep(2)
        print('校验完毕...')

        # 调用原函数
        func(*args, **kwargs)

    return wrapper


@decorate
def f3(student, x):
    print(x)
    for stu in student:
        print(stu)


@decorate
def f1():
    print('------f1-----')

@decorate
def f2(a, b):
    print('-----f2---', a, b)


# f1()
# f2(1, 2)
li = [1, 2, 3, 4]
f3(li, x=1)