# def add(*args):
#     if len(args) > 0:
#         sum = 0
#         for i in args:
#             sum += i
#         return sum
#     else:
#         return "value error"
#
#
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))
# def add(name, age, *args):
#     if len(args) > 0:
#         sum = 0
#         for i in args:
#             sum += i
#         return f'{name}累加和是{sum}'
#     else:
#         return "value error"
#
#
# print(add('haha', 1, 2, 3, 4))

# 注意：可变参数必须放在后面
# print(add('guagua', 1))
# print(add('guag'))
#


# 可变参数 + 关键字参数

# 关键字参数：key=value
#
# def add(a, b=10):  # 关键字参数
#     result = a + b
#     print(result)
#
#
# add(1)
#
# add(4, 7)  # 覆盖
#
#
# def add1(a, b=10, c=4):
#     result = a + b + c
#     print(result)
#
#
# add1(1)
# add1(1, 5)  # 赋值给b
#
# # 给c赋值而不是b赋值
# add1(2, 6)  # 2赋值给a，6赋值给b
# add1(2, c=6)  # 定向赋值，结合关键子key使用
#
# 答应每位同学的姓名和年龄
student = {
    '001': ('iKun', 20),
    '002': ('王俊凯', 18),
    '003': ('潘周单', 39),
    '004': ('周某人', 20)
}


def print_boy(**persons):
    if isinstance(persons, dict):
        values = persons.values()
        for name, age in values:
            print(f'姓名：{name},年龄：{age}')


# 调用
print_boy(**student)

# def func(**kwargs):  # 关键字参数 key word arguments
#     print(kwargs)
#

# func()
# func(a=1, b=2, c=3)  # 关键字参数：成对出现，传参时，key=values 满足此类格式才能传入函数
# func(a='a', b ='b', c='c')
# # *args 传入时默认为元组
# # **kwargs 传入时默认为字典
#
# # 若是放字典则在字典前加**  eg: func(**dict)
# dic = {'a':'python', 'b':'java', 'c':'C语言'}
# func(**dic)