# 异常情况
"""
格式一：在不报错的情况下执行else里面的代码
try:
    pass
except:
    pass
else:
    pass

格式二：是否报错，都执行finally里面的代码，finally优先级比return高
try:
    pass
except:
    pass
finally:
    pass
"""


def func():
    stream = None
    try:
        stream = open(r"D:\pythonDir\test\aa.txt")
        container = stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('-------finally--------')
        if stream:
            stream.close()
        return 3


print(func())