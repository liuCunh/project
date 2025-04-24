# 小案例
# s = "哈哈3s2d"
# result = re.search("[0-9][a-z]", s)
# print(result)

msg = "abcd7y ikfd8hdf00"
result = re.search("[a-z][0-9][a-z]", msg)  # a-z 从a到z search()只能查找一次
print(result)

result = re.findall("[a-z][0-9][a-z]", msg)  # 查找所有，匹配整个字符串
print(result)


# 第一个正则的符号
# 筛选规则 字母(1个)数字(n个)字母(1个)
msg = "a7aopa88ak ggka7578a"
result = re.findall("[a-z][0-9]+[a-z]", msg)  # 针对个数的 +号放在后面表示该个数>=1, *表示出现次数大于等于0 >=0
print(result)

# 验证qq号，首位不能为0
# '{m}' 用于验证前面的模式匹配m次, "{m, }"用于验证前面的模式匹配m次或者多次 >= m
# {m, n}"用于验证前面的模式匹配大于m次并且小于等于n次
qq = "45208012321"
result = re.match("^[1-9][0-9]{4,10}$", qq)  # {4}该个数自能出现4次，^ 表示字符串开头， $ 表示字符串结尾
print(result)