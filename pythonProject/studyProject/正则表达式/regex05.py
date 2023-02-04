# 不以4，7结尾的手机号(11位)
import re

# 整体匹配一定要加$符号
num = "15082699768"
result = re.search(r"1\d{9}[^47]$", num)
print(result)

# 爬虫
# group() 分组匹配，正则中必须要右分组符号(), 访问下标从1开始
phone = "010-12345678"
result = re.match(r"(\d{3})-(\d{8})$", phone)
print(result)

print(result.group())  # 整体
print(result.group(1))  # 第一组
print(result.group(2))  # second group


msg = "<html><h1>abc</h1></html>"
msg1 = "<h1>hello</h1>"
result = re.match(r"<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>", msg)  # .表示任意字符
print(result)
print(result.group(1))


# number
result = re.match(r"<([0-9a-zA-Z]+)>(.+)</\1>$", msg1)  # .表示任意字符， \1表示引用第一组的内容让\1所在位置的字符串跟第一组相同
print(result)
print(result.group(1))
print(result.group(2))

msg = "<html><h1>abc</h1></html>"

result = re.match(r"<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$", msg)
print(result)
