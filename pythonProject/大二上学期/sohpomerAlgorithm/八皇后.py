"""
规则：
 1、不同行
 2、不同列
 3、不同对角线
"""


def rule(col, row):
    """
    :param col:
    :param row: 当前行
    :return:
    """
    for i in range(row):
        # 如果列相同就返回False
        if col[i] == col[row]:
            return False
        # 如果在同意对角线，也返回False
        # col[i]-col[row]列差， i-row行差
        elif abs(col[i] - col[row]) == abs(i - row):
            return False
    return True


# 生成棋盘
def board(col, n, row, x):
    """
    :param col: 列表， 索引代表行，数据代表列
    :param n: 行数
    :param row: 当前的行数
    :return:
    """
    global count
    if row == n:
        col = [x+1 for x in col]
        count += 1
        if count == x:
            print(f"col={col}")
        return
    for i in range(n):
        col[row] = i  # 在列上放上皇后
        if rule(col, row):
            board(col, n, row + 1, x)

n = 4
x = 1
count = 0
board([None] * n, n, 0, x)
print(count)
