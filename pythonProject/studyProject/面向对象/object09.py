# __str__ 触发时机：当打印对象名的时候自动触发return的内容


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name: {self.name}, age: {self.age}'


p = Person("Tom", 18)
print(p)

"""
总结魔术方法
重点：
    __init__,：构造方法：创建完空间后的第一个调用的方法
    __str__
了解：
    __new__：开辟空间；
    __del__：没有指针引用的时候调用，大部分情况下不用重写
    __call__: 是否将对象当初函数使用
"""