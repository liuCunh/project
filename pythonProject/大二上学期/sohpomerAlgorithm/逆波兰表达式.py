def RPn_add(li):  # 将列表中的+-运算先进行处理 eg:["*", "+", 11, 12, "+", 24, 35], 处理后["*", 23, 59]

    #  快慢指针：slow指向+-索引的位置，fast指向运算的数字。eg：[+,11,12] slow=0, fast=2
    slow, fast = 0, 2

    # 找到列表中第一个+-号出现的位置
    while fast < len(li) and not (li[slow] in ['-', "+"]):
        slow += 1
        fast += 1

    # 对列表的数据进行加减合并： eg: ["+", 11, 12] 处理后[23]
    if li[slow] == "-":
        res = li[slow + 1] - li[fast]
        li[slow:fast + 1] = [res]
        return RPn_add(li)
    elif li[slow] == "+":
        res = li[slow + 1] + li[fast]
        li[slow:fast + 1] = [res]
        return RPn_add(li)
    else:
        return


def RPn_mul(li):  # 进行*/运算
    slow, fast = 0, 2

    # 当列表中只剩下一个元素的时候就为最后结果
    if fast > len(li):
        return li[-1]

    if li[slow] == "*":
        res = li[slow + 1] * li[fast]
    else:

        # 除数不能为0
        try:
            res = li[slow + 1] / li[fast]
        except ZeroDivisionError:
            return

    # 对列表的数据进行乘除合并： eg: ["*", 3, 4] 处理后[12]
    li[slow:fast + 1] = [res]
    return RPn_mul(li)


if __name__ == '__main__':
    li = ["*", "+", 11, 12, "+", 24, 35]
    RPn_add(li)  # 处理列表中的所有加减法
    res = RPn_mul(li)  # 剩余的乘除法先后进行计算
    print(res)
