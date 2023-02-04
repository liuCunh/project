# 分组
import re

# 匹配数字0-100数字
n = '09'

# result = re.match(r"[1-9]?\d", n)
result = re.match(r"[1-9]?\d?$|100$", n)  # | 或者,前后都要加$符号
print(result)

# 验证邮箱163 126 qq
# 匹配一定要记得正则匹配
email = "1508585459@qq.com"

# () 整体字符匹配，[]单个字符匹配， eg: (word|word|word|) 表示一个单词之间的或者， [abc]表示一个字母之间的范围
result = re.match(r"\w{5,20}@(163|qq|126)\.(com|cn)$", email)
# print(result)


