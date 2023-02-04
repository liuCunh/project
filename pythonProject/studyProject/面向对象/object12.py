# 继承： is a, has a
"""
1、has a
    一个类中使用了另外一个自定义的类型

    student使用computer

2、典型
    系统类型：
        str int float
        list dict tuple set
    自定义类型：
        算是自定义的类型，都可以将起当成一种类型
        s = Student()
        

"""

class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print("正在使用电脑上网！")

    def __str__(self):
        return self.brand + "----" + self.type + "----" + self.color


class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + "-----" + self.author + "-----" + str(self.number)


class Student:
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            if book1.bname == book.bname:
                print("已经借过这本书了")
                break
        else:
            # 将参数book添加到列表
            self.books.append(book)
            print("添加成功!")


    def show_book(self):
        for book in self.books:
            print(book.bname, end=",")

    def __str__(self):
        return self.name + str(self.computer) + str(self.books)


# 创建对象
computer = Computer("Mac", "Mac Pro 2018", "深灰色")
book = Book("盗梦空间", "南派三叔", 10)
stu = Student("小米", computer, book)
print(stu)

book1 = Book("鬼吹灯", "天下霸唱", 8)
stu.borrow_book(book1)


stu.show_book()

