class Student:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def eat(self):
        print(f'{self.name}正在吃饭')

    def study(self):
        print(f'{self.school}学习氛围真好，都晚上11点了，{self.name}还在学习')

    def __str__(self):
        return f'姓名：{self.name}，年龄：{self.age}，学校：{self.school}'


s = Student("刘春", 20, "重庆航天职业技术学院")
s.eat()
s.study()
print(s)
