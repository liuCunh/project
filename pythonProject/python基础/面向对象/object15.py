# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print("--------eat---1")
#
#     def eat(self, food):
#         print("-------eat---2", food)
#
#
# p = Person("Jack")
# p.eat("满汉全席")

# 多继承
# class Base:
#     def test(self):
#         print("-------Base-------")
#
# class A(Base):
#     def test(self):
#         print("---AAAAAAAA")
#
# class B(Base):
#     def test(self):
#         print("----BBBBBB")
#
# class C(Base):
#     def test(self):
#         print("---------CCCCCCC")
#
# class D(A, B, C):
#     pass
#
# d = D()
# d.test()
#
# import inspect
#
# print(inspect.getmro(D))  # 继承对象
# print(D.__mro__)
"""
多继承的搜索顺序： 经典类 新式类

"""

# 经典类：从左到右，深度优先
# class P1:
#     def foo(self):
#         print("P1---foo")
#
#     def bar(self):
#         print("P1---bar")
#
#
# class P2:
#     def foo(self):
#         print("P2---foo")
#
#
# class C1(P1, P2):
#     pass
#
#
# class C2(P1, P2):
#     def bar(self):
#         print("C1---bar")
#
#
# class D(C1, C2):
#     pass


# d = D()
# print(D.__mro__)
# d.foo()  # p1
# d.bar()  # c2

# 新式类
class P1(object):
    def foo(self):
        print("P1---foo")

    def bar(self):
        print("P1---bar")


class P2(object):
    def foo(self):
        print("P2---foo")


class C1(P2):
    pass


class C2(P2):
    def bar(self):
        print("C1---bar")


class D(C1, C2):
    pass


d = D()
print(D.__mro__)