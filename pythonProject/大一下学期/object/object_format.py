# 面向对象：类==》创建对象==》调用对象
# 定义类==》 class 类名： 类名采用大驼峰命名 eg: StudentName 前后单词首字母都要大写
class test:
    # 创建属性==> 属性名：值
    name = '张三'
    age = 18
    # 创建过程==》 def 过程名(self): 过程名采用小驼峰命名 eg: studentName 前面单词首字母小写后面单词首字母大写
    def student(self):
        print('hello')
# 创建对象==》 对象名:类名()
studentName = test()
# 调用对象==》
    # 调用属性： 对象名.属性名
    # 调用过程： 对象名:对象名()
print(studentName.name)
print(studentName.age)
studentName.student()
