class Person:
    name = '张三'

    def __init__(self, name, age):
        self.name = '张三'
        self.age = 18

    def eat(self, food):
        print(f'{self.name}正在吃{food}')

    def run(self):
        print(f'{self.name}今年{self.age}正在跑步')


p1 = Person('lisi', 20)
p1.name = '李四'
p1.eat('火锅')
p1.run()
