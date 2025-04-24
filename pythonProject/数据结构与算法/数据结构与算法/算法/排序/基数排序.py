"""
多关键字排序：假如现在有一个员工表，要求按照薪资排序，年龄相同的员工按照年龄排序。
先按照年龄进行排序，再按照薪资进行稳定的排序
对32，13，94，52，17，54，93排序，是否可以看作是多关键字排序
"""
def radix_sort(li):
    max_num = max(li)
    it = 0  # 标识最大数的位数

    # 对列表进行排序
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]  # 0~9存储十个桶

        # 数字进行装桶
        for var in li:
            digit = (var // 10 ** it) % 10  # ((var//10^it):取出十位、百位、千位...对应的数字 % 10):对取出的数字进行装桶
            buckets[digit].append(var)
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1


import random
li =[random.randint(0, 4) for _ in range(10)]
print(li)
radix_sort(li)
print(li)