# is a
"""
继承：
    Student, Employee, Doctor ---> 都属于人类
    相同代码 ---> 代码冗余，重复性高

    将相同的代码提取---》 Person
        Student, Employee, Doctor --》 继承Person
        class Sudent(Person):
            pass
    特点：
        1、如果类中不定义__init__()，则调用父类的 super class 中的__init__()
        2、如果类继承父类，也需要初始化自己的变量，则就在__init__()方法中使用super() 传入父类的初始化变量
        3、如何调用父类的__init__()
            super().__init__(参数)
            super(类名， 对象).__init__(参数)
        4、如果子类中含有父类的方法，默认搜素原则：先找子类，在去找父类
            这个过程被称为：overrider(重写，覆盖)
            父类提供的方法不能满足子类需求，就需要在子类中定义一个同名的方法，这种行为被称为：重写
        5、子类的方法中也可以调用父类的方法：
            super().方法名(参数)

"""


# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 18
#
#     def eat(self):
#         print(f"{self.name}正在吃饭")
#
#     def run(self):
#         print(f"{self.name}正在跑步")
#
#
# class Student(Person):
#     def __init__(self, name):
#         print(f'-------Student的init')
#         super(Student, self).__init__(name)  # super() 父类对象
#
#
# class Employee(Person):
#     pass
#
#
# class Doctor(Person):
#     pass
#
#
# s = Student("Jack")
# s.run()
#
# e = Employee("Lily")
# e.run()
#
# d = Doctor("Tom")
# d.run()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃饭")

    def run(self):
        print(f"{self.name}正在跑步")


class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)
        self.clazz = clazz

    def study(self, course):
        print(f"{self.name}正在学习{course}")

    def eat(self, food):
        super().eat()
        print(f"{self.name}正在吃{food}： 喜欢吃满汉全席")


class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super(Employee, self).__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients


s = Student("Jack", 18, "大数据一班")
s.run()
s.study("Python基础")
s.eat("大逼斗")

e = Employee("Tom", 24, 10000, "Boss")

lists = ["张三", "lisi", "zhaoliu"]
Doctor("Lucy", 50, lists)
