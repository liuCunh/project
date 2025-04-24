"""
一个小偷在某个商店发现有n个商品，第i个商品价值v元，重w千克，他希望拿走的价值尽量高，但他的背包
最多只能容纳w千克的东西。他应该拿走那些商品？
 0-1背包：对于一个商品，小偷要么将它完整拿走，要么留下。不能只拿走一部分，或把一个商品拿走多次(商品为金条)
 分数背包：对于一个商品，小偷可以拿走任意一部分(商品为金沙)factional_backpack
"""
goods = [(60, 10), (120, 30), (100, 20)]  # (商品价格， 商品重量)
goods.sort(key=lambda x: x[0] / x[1], reverse=True)


def factional_backpack(goods, w):  # goods商品价格跟重量，w：背包重量
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (price, weight) in enumerate(goods):
        if weight < w:
            m[i] = 1
            w -= weight
            total_v += price
        else:
            m[i] = w / weight
            total_v += price * m[i]
    return m, total_v


# print(factional_backpack(goods, 50))

# 第二次写
goods = [(60, 10), (100, 20), (120, 30)]
goods.sort(key=lambda x: x[0] / x[1], reverse=True)


def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_price = 0
    for ind, (price, weight) in enumerate(goods):
        if w >= weight:
            m[ind] = 1
            total_price += price
            w -= weight
        else:
            m[ind] = w / weight
            total_price += price * m[ind]
            break
    return m, total_price


print(fractional_backpack(goods, 50))
