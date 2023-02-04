# 私有化
# 封装：1、私有化属性 2、定义公有set和get()方法
# __属性：将属性私有化，访问范围仅仅限于类中
"""
优点：
1、隐藏属性不被外交随意修改
2、也可以修改：通过函数来修改
    def setXX(self, XX)：
3、赛选内容，看值是否满足条件
4、如果想获取一个具体的属性
    使用get()函数
    getXXX(self):
        return self.XXX

"""


class Student:
    # __age = 18

    def __init__(self, name, age):
        self.__name = name  # 长度必须六位
        self.__age = age
        self.__score = 59

    # 定义共有的set和get()方法
    # set为了赋值
    def setAge(self, age):
        if 0 < age <= 120:
            self.__age = age
        else:
            print("无效的年龄")

    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print("名字长度不为6")

    def setScore(self, score):
        pass

    # get() 为了取值
    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def __str__(self):
        return f'name: {self.__name}, age: {self.__age}, score: {self.__score}'


liuchun = Student("liuchun", 20)
liuchun.setAge(21)
print(liuchun.getName())
print(liuchun)
print(dir(Student))
print(dir(liuchun))
print(__name__)


