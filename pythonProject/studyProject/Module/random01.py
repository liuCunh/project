import random

ran = random.random()  # 得到0到1之间的随机小数
print(ran)

ran = random.randrange(1, 10)  # 产生一个range范围的随机数
print(ran)

ran = random.randint(1, 10)
print(ran)

list1 = ["Tom", "Jack", "Lily", "Jerry"]
ran = random.choice(list1)  # 随机选取sequence中的值
print(ran)

pai = ["♥A", "♦K", "♣J", "♠Q"]
random.shuffle(pai)
print(pai)

s = "alkjf38jlasjdf832984jfa03487"
# 验证码
def func():
    code = ""
    for i in range(4):
        ran1 = str(random.randint(0, 9))
        ran2 = chr(random.randint(65, 90))
        ran3 = chr(random.randint(97, 122))

        r = random.choice([ran1, ran2, ran3])
        code += r
    return code


print(func())


