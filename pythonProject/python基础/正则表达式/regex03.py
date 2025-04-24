import re

username = "$%@admin001￥%@"
# result = re.search("^[a-zA-Z][0-9a-zA-Z]{5,}$", username)
result = re.search("^[a-zA-Z]\\w{5,}$", username)

# 当^出现在[]中是表示逻辑非 eg: [^0-9] 不是0-9的数字
print(result)

msg = "aa*py ab.txt bb.py kk.png uu.py apyh.txt"
# result = re.findall("py\\b", msg)  # \\b是因为字符串在遇\时会进行转义，\b转义后被程序读取为其他意思了，\\b才能为程序读取为\b操作
result = re.findall(r"\w+\.py\b", msg)  # .表示任意字符
print(result)

"""
. 除\n之外的任意字符
^ 开头
$ 结尾
[] 范围 eg: [abc] [a-z] [a-z*%!]

正则预定义:
    \s 空格
    \S 非空格
    \b 边界
    \d 数字
    \D 非数字
    \w word [0-9a-zA-Z_]
    
    '\w[0-9]'  --> \w [0-9] 只能匹配一个字符

量词：
    * >=0
    + >=1
    ? 0,1
    
手机号码正则：re.match("^1[3579]\d{9}$", phone)
{m} 固定m位
{m,} >=m
{m,n} m <= phone <= n


"""
