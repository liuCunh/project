# 全局变量不可变在函数中修改需要添加global关键字
# 全局变量为可变类型，在函数中修改时不用加关键字
name = '月月'
list1 = [1, 2, 3, 4]
def func():
    name = 'guagua'

    print(name)
    print(list1)

def func1():
    global name
    print(name)
    name = 'very beautiful'

    list1.append(8)
    print(list1)

func1()
