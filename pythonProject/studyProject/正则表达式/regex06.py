# 起名的方式
"""
起名
    (?P<名字>正则)  (?P=name)

"""
import re

msg = "<html><h1>abc</h1></html>"

result = re.match(r"<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>", msg)  # 命名方式的正则
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))

"""
分组： ()  result.group(1) 获取组中的匹配内容
不需要引用分组
    <([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$"
引用分组匹配内容：
    1 number \number 引用第number组的内容 
    <html><h1>abc</h1></html>
"""

# regex:正则规则 string:修改字符串
# sub(regex, "新内容"， string)
def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


result = re.sub(r"\d+", func, "java:99, python:100")
print(result)


# split() 在字符串中搜索，如果遇上正则中的内容就进行分割，保存在列表中
result = re.split(r"[,:]", "java:99, python:100")
print(result)