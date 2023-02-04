# 某公司出售钢条，出售价格与钢条长度之间的关系如下表：
# (1, 1), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17)， (8, 20), (9, 24), (10, 30) (长度，价格)
# 问题：现在有一段长度为n的钢条和上面的价格表，求切割钢条方案，使得总收益最大
import time
import sys
sys.setrecursionlimit(100000)


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# 自顶向下实现
def cur_rod_recurision_1(p, n):
    if n == 0:
        return 0
    else:

        # 用程序写出算法公式一
        res = p[n]
        for i in range(1, n):
            res = max(res, cur_rod_recurision_1(p, i), cur_rod_recurision_1(p, n-i))
        return res


@cal_time
def c1(p, n):
    return cur_rod_recurision_1(p, n)

# 自顶向下实现
def cur_rod_recurision_2(p, n):
    if n == 0:
        return 0
    else:
        # 用程序写出算法公式二
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i] + cur_rod_recurision_2(p, n-i))
        return res


@cal_time
def c2(p, n):
    return cur_rod_recurision_2(p, n)

@ cal_time
def cut_rod_dp(p, n):  # 基于算法公式二的非递归方法
    r = [0]
    for i in range(1, n+1):
        res = 0
        for j in range(1, i+1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]


def cut_rod_extend(p, n):
    r = [0]
    s = [0]  # 要被切割的长度
    for i in range(1, n+1):
        res_r = 0  # 价格的最大值
        res_s = 0  # 价格最大值对应方案的左边不切割部分的长度
        for j in range(1, i+1):
            if p[j] + r[i-j] > res_r:
                res_r = p[j] + r[i - j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s


def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    method = []
    while n > 0:
        method.append(s[n])
        n -= s[n]
    return method


r, s = cut_rod_extend(p, 20)
print(r)
print(cut_rod_solution(p, 20))

