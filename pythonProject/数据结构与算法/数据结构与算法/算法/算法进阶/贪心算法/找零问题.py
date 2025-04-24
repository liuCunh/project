# 假设商店老板需要找零n元钱，钱币的面额有：100元、50元、20元、5元、1元，如何找零使得所需的钱币数量最少
def myself(s):
    money = [100, 50, 20, 5, 1]
    count = 0
    for i in money:
        count = count + s // i
        s %= i
    print(count)


def movie(s, n):
    li = [0 for _ in range(len(s))]
    for i, money in enumerate(s):
        li[i] = n // money
        n %= money
    return li, n


# 第二次写
t = [100, 50, 20, 5, 1]


def my_second(t, n):
    money_total = [0 for _ in range(len(t))]
    for ind, money in enumerate(t):
        money_total[ind] = n // money
        n %= money
    return money_total, n


# li = [100, 50, 20, 5, 1]
# print(movie(li, 376))
print(my_second(t, 376))
