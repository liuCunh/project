# 静态方法
"""
静态方法：跟类方法非常相似
1、需要装饰器@staticmethod
2、静态方法不用传递self。cls
3、也只能访问类的属性跟方法，对象是无法访问的
4、加载时机同类方法

总结：
类方法和静态方法
不同：
    1、装饰器不同
    2、类方法含cls参数，而静态方法不含参数
相同：
    1、只能访问类的属性和方法，对象的是无法访问的
    2、都可以通过类名访问
    3、都可以在创建对象之前访问，因为是不依赖于对象的

普通方法与两者的区别：
不同：
    1、没有装饰器
    2、普通方法永远依赖对象，因为每个普通方法都有一个self
    3。只有创建了对象才能调用普通方法，否则无法调用
"""


class Person:
    __age = 18

    def __init__(self):
        self.name = "Jack"

    def show(self):
        print('------>', Person.__age)

    @classmethod
    def update_age(cls):
        cls.__age = 20
        print('--------类方法-------')

    @classmethod
    def show_age(cls):
        print('修改后的年龄：', cls.__age)

    @staticmethod
    def test():
        print('-------静态方法--------')
        # print(self.name)  语法错误
        print(Person.__age)

# p = Person()
# p.age += 1
# p.show()
Person.update_age()
Person.show_age()
Person.test()