# 求最大公约数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd1(a, b):
    while b > 0:
        res = a % b
        a = b
        b = res
    return a


print(gcd1(12, 16))
