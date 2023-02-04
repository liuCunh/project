# 有n个非负整数，将其按照字符串拼接的方式拼接为一个整数。如何拼接可以使得得到的整数最大？
#  例如：32，94，128，1286，6，71可以拼接出的最大整数为：94716321286128
from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]


def myself(li):
    s = ''
    li.sort(key=lambda x: max(str(x)[0]), reverse=True)
    for i in li:
        s += "".join(str(i))
    return s


def xy_cmp(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def number_join(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    return ''.join(li)


def xy_cmp2(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def my_second(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp2))
    return ''.join(li)


# print(number_join(li))
print(my_second(li))
