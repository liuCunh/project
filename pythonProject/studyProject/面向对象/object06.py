# 类方法
"""
特点；
    1、定义需要依赖装饰器classmethod
    2、类方法中参数不是一个对象，而是类
        print(cls)  # --> <class '__main__.Dog'>
    3、类方法中只能使用类属性
    4、类方法中不可用普通方法
类方法作用：
    只能类属性和方法，可以在对象创建之前，如果需要完成一些动作(功能)
"""


class Dog:
    aa = 'haha'

    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):
        print(f'{self.nickname}在院子里跑来跑去')

    def eat(self):
        print('吃饭')
        self.run()  # 类中调用方法，需要通过self.方法名()

    @classmethod
    def test(cls):  # cls class
        print(cls.aa)
        print(cls)  # --> <class '__main__.Dog'>
        # print(cls.nickname)


Dog.test()
Dog.eat(Dog('大黄'))


# d = Dog('大黄')
# d.run()
# d.test()
class Person:
    __age = 18

    def show(self):
        print('------>', Person.__age)

    @classmethod
    def update_age(cls):
        cls.__age = 20
        print('--------类方法-------')

    @classmethod
    def show_age(cls):
        print('修改后的年龄：', cls.__age)


# p = Person()
# p.age += 1
# p.show()
Person.update_age()
Person().show()
