# 封装 继承 多态  --> 面向对象
class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):
        # isinstance(obj, cls)  --> 判断ojb是否为cls的对象或判断obj是否为cls的子类
        if isinstance(pet, Pet):

            print(f"{self.name}喜欢养宠物{pet.role}, 宠物名是：{pet.nickname}")
        else:
            print("不是宠物类型，养了要背时")


class Pet:
    role = "Pet"
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print(f"宠物名：{self.nickname}， 年龄：{self.age}")


class Cat(Pet):
    role = "猫"
    def catch_mouse(self):
        print("抓老鼠")


class Dog(Pet):
    role = "狗"
    def watch_house(self):
        print("看家高手")

class Tiger:
    def eat(self):
        print("太可怕了，可以吃人！")

# 创建对象
cat = Cat("花花", 2)

dog = Dog("大黄", 4)

person = Person("刘春")
person.feed_pet(cat)


person = Person("花花", )
person.feed_pet(Tiger)