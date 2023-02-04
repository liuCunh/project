"""
[] 表示一个范围

"""

# qq = input("输入QQ号码：")
# if len(qq) >= 5 and qq[0] != "0":
#     print("合法的")
# else:
#     print("无效的QQ号")
import re

# # match的底层实现
# msg = "佟丽娅娜扎热巴代斯"
# pattern = re.compile("佟丽娅")
# result = pattern.match(msg)  # 没有匹配
# print(result)
#
# # 使用正则re模块方法： match
# s = "娜扎热巴代斯佟丽娅"
# result = re.match("佟丽娅", s)  # 从开头进行匹配，如果匹配不成功则返回None
# print(result)
#
# # 使用正则re模块方法： search
# result = re.search("佟丽娅", s)  # 匹配整个字符串(不限于位置)，跟match相似
# print(result)
#
# print(result.span())  # 返回位置下标
#
# print(result.group())  # 使用group提取匹配到的内容
# print(result.groups())

#