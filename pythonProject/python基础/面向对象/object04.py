# 函数 和 类里面定义的：方法
class Phone:
    # 魔术方法之一：出现魔术方法时系统默认执行， __名字__() 这个类型的都是魔术方法
    def __init__(self):
        self.brand = 'xiaomi'
        self.price = 4999

    def call(self):  # self不断变化
        print("--------call--------")
        print(f'价格{self.price}')


p1 = Phone()
p1.call()
p1.price = 5999
p1.call()