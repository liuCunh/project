"""
装饰器多层，距离函数最近，就优先使用那个装饰器
"""

def zhuang1(func):
    print('-----start zhuang1')

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('刷漆')

    print('----end-----')
    return wrapper


def zhuang2(func):
    print('-----start zhuang2')

    def wrapper(*args, **kwargs):
        func()
        print('铺地板，装门')

    print('-----end-----')
    return wrapper


@zhuang2
@zhuang1
def house():
    print('我是毛坯房')


house()
