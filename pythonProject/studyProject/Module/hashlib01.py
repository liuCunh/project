# 加密算法 md5, sha1, sha256
# base64可以反向解码
import hashlib

msg = "某某今天中午一起吃饭！"

# 加密
md5 = hashlib.md5(msg.encode("utf-8"))  # 用md5算法给信息加密
print(len(md5.hexdigest()))  # 将加密后的数据转化为六进制

sha1 = hashlib.sha1(msg.encode("utf-8"))
print(len(sha1.hexdigest()))

sha256 = hashlib.sha256(msg.encode("utf-8"))
print(len(sha256.hexdigest()))

password = "123456"
list1 = []
sha256 = hashlib.sha256(password.encode("utf-8"))
list1.append(sha256.hexdigest())

pwd = input("enter password:")
sha256 = hashlib.sha256(pwd.encode("utf-8"))
pwd = sha256.hexdigest()
print(pwd, list1)
for i in list1:
    if pwd == i:
        print("登录成功！")