# 装饰器带参数
"""
带参数的装饰器的三层
最外层的函数负责接收装饰器参数
里面的内容还是原装饰器内容
"""


def outer(a):  # 第一层：接受装饰器的参数
    def decorate(func):  # 第二层：接收函数的
        def wrapper(*args, **kwargs):  # 第三层：接收函数的参数
            func(*args, **kwargs)
            print('-----装修----费用-->', a)

        return wrapper  # 返回第三层

    return decorate  # 返回第二层


@outer(10)
def house(time):
    print(f'我{time}拿到了钥匙，是毛坯房')


# house('2022-08-26')

@outer(100)
def street():
    print(f'新秀路铺路费用--》')


street()
