# 魔术方法
# __init__()
"""
__new__() 实例化的魔术方法: 向内存要空间--> return 地址
__call__() 对象调用方法。触发时机：将对象当作函数使用时调用的魔术方法 eg: p=Person() p()
__del__() 析构魔术方法, 当对象没有用(没有任何变量引用)的时候触发
    1、对象赋值
        p = Person()
        p1 = p 说明：p和p1指向同一个地址
    2、删除地址引用
        del p1 删除p1对地址的引用
    3、查看地址引用次数
        import sys
        sys.getrefcount(p)
    4、当一块空间没有任何的引用，默认执行__del__方法
"""


class Person:
    def __init__(self, name):
        self.name = name
        print('----------init self: ', self)

    def __new__(cls, *args, **kwargs):
        print('----------->new方法')
        position = object.__new__(cls)
        print('------->new self: ', position)
        return position

    def __call__(self, name):
        print('-----------now in call')
        print('执行对象得到的参数是：', name)


p = Person('as')

print('----------object p: ', p)

p('hello')  # 这里时call魔术方法的调用


# 下面是对__del__的说明

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'-------del被执行-------')


p = Person("Jack")
import sys

p1, p2 = p, p
p1.name = "Tom"
del p2, p1
print("删除p1之后的结果：", p.name)


print(sys.getrefcount(p))  # 获取对象的引用个数
