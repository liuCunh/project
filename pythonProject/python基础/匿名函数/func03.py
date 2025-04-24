# 手动测试减法
list1 = [1, 2, 3, 5, 92, 49, 12]
result = filter(lambda x: x > 10, list1)

print(list(result))

# list2 = []
# for i in list1:
#     if i>10:
#         list2.append(i)
#
# print(list2)
stu = [
    {'name': 'tom', 'age': 10},
    {'name': 'Lucy', 'age': 19},
    {'name': 'lily', 'age': 39},
    {'name': 'mark', 'age': 31},
    {'name': 'jack', 'age': 21},
    {'name': 'stare', 'age': 12}
]
res = filter(lambda x: x['age'] > 20, stu)
print(list(res))

stu = sorted(stu, key=lambda x: x['age'])
print(stu)

"""
总结：
max()
min()
sorted()

map() 对列表中的每一个元素进行操作
filter() 过滤
reduce()  列表元素进行累加，减等操作

"""
