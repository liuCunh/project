__all__ = ["add", "number", "Calculat"]
number = 100
name = "calculat"


def add(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum += i
        return sum
    else:
        print("相加至少含有两个参数")


def miuns(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m += i
        return m
    else:
        print("相减至少含有两个参数")


def multiply(*args):
    pass


def divide(*args):
    pass


class Calculat:
    def __init__(self, num):
        self.num = num

    def test(self):
        print("正在使用calculat进行运算")

    @classmethod
    def test1(cls):
        print("calculate中的类方法")


def test():
    print("我是测试")

print("__name__:----->",__name__)
if __name__ == '__main__':
    # print(__name__) # __name__ = __main__
    test()
