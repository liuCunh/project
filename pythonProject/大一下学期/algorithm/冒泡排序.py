def compare():
    global swap, inCount
    swap = True
    inCount += 1


# s = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]
# s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# s = [3, 0, 1, 2, 4, 9, 5, 8, 6, 7]
s = [2, 4, 3, 9, 7, 5, 1, 8, 6, 0]
count = 0  # 内测循环次数
judge = 0  # 交换次数
maxIndex = len(s)  # 这个索引的初始值应为len(s)-i

for i in range(len(s)-1):
    swap = False  # 排序第一次，最大值就已经在末尾，所以下一次比较就不用在比较上一次比较出来的最大值，这里为了较少循环次数

    # 从一开始为了避免超过范围
    for j in range(1, maxIndex):
        count += 1  # 统计内测次数

        # 判断前后大小关系
        if s[j-1] > s[j]:
            swap = True  # 跳转标识符
            s[j-1], s[j] = s[j], s[j-1]  # 谁小谁在前面
            maxIndex = j
            judge += 1  # 统计交换次数

    # 末尾最大值结束循环
    if not swap:
        break

print(f'最后结果是：{s}')
print(f'内测运算{count}次，交换次数{judge}')
