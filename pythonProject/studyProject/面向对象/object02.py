# 定义类和属性
class Student:
    # 类属性
    name = 'xiaowei'
    age = 2


xiaowei = Student()
xiaowei.age = 18  # 对象属性
print(xiaowei.age)

yupeng = Student()
print(yupeng.name)
yupeng.name = '(*^_^*)'
print(yupeng.name)
print(yupeng.age)

yupeng.age = 1
print(yupeng.age)

print(xiaowei.age)

Student.name = 'feifei'  # 更改类属性
ruirui = Student()
print(ruirui.name)
