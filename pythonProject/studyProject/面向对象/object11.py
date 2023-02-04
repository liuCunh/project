class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 实现私有属性调用和修改跟普通属性一样
    # 先getXXX
    @property
    def age(self):
        return self.__age

    # 再有set，因为set依赖于get
    @age.setter
    def age(self, age):
        if 0 < age <= 100:
            self.__age = age
        else:
            print("名字不符合规范！")
    # def setAge(self, age):
    #     if 0 < age <= 100:
    #         self.__age = age
    #     else:
    #         print("名字不符合规范！")
    #
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return f"name: {self.name}, age: {self.__age}"


s = Student("liuchun", 20)
s.name = "小刘"

print(s.__dir__())
print(s.age)

s.age = 10
print(s.age)

# # 私有化赋值
# s.setAge(21)
# print(s.getAge())
