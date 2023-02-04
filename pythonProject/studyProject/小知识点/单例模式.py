# 单例模式: 一种开发模式
# class Student:
#     pass
#
#
# s = Student()
# s1 = Student()
# print(s)
# print(s1)

class SingleTon:
    # 私有化
    __instance = None
    name = "Jcak"

    # 重写 __new__
    def __new__(cls):
        print("----------new----------")
        if cls.__instance is None:
            print("----这里为空哦-------")
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            print("-----这里不为空")
            return cls.__instance

    def show(self, n):
        print("-----name: ", SingleTon.name, n)



s = SingleTon()
s1 = SingleTon()
print(s)
print(s1)
s.show(6)
s1.show(5)