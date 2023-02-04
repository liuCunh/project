# 列表推导式  字典推导式  集合推导式
# 旧列表 --> 新列表


# 列表推导式  格式：[表达式 for 变量 in 旧列表]
# 或者 [表达式 for 变量 in 旧列表 if 条件]

# 过滤掉长度小于或者等于3的人名
names = ['tom', 'abc', 'hahha', 'jack', 'alix', 'bbb']
result = [name for name in names if len(name) > 3]
print(result)
"""
def func(names):
    res = []
    for name in names:
        if len(name)>3:
            res.append(name)
    return res
"""

# name.capitalize() 将首字母大写，类似于 s.title()
res = [name.capitalize() for name in names if len(name) > 3]
print(res)

# 将1到100之间能被3整除，组成一个列表
newlist = [i for i in range(1, 101) if i % 3 == 0]
print(newlist)

# [(偶数，奇数), (), ()]  -->[(0,1), (0, 3), (0,5), (0, 7), (0, 9), (2, 1)]
"""
def func():
    newlist = []
    for i in range(5):
        if i % 2 == 0:
            for j in range(10):
                if j % 2 != 0:
                    newlist.append((i, j))
    return newlist
"""
newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(newlist)

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]  # return -- > [3, 6, 9, 5]
li = [i[-1] for i in list1]
# def func(li):
#     res = []
#     for i in range(len(li)):
#         res.append(li[i][-1])
#     return res
# print(func(list1))

dict1 = {'name':'tom', 'salary': 3500}
dict2 = {'name':'Lucy', 'salary': 5000}
dict3 = {'name':'Jack', 'salary': 8000}
dict4 = {'name':'Lily', 'salary': 4200}
list1 = [dict1, dict2, dict3, dict4]
# 薪资大于5000加200， 小于等于5000加500
new = [i['salary']+200 if i['salary'] > 5000 else i['salary']+500 for i in list1]
print(new)
"""
for employee in list1:
    if employee['salary'] > 5000:
        employee['salary'] += 200
    else:
        employee['salary'] += 500
print(list1)
"""
