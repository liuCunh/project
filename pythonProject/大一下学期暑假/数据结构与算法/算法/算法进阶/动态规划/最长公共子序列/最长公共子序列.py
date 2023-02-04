# 一个序列的子序列是在该序列中删去若干元素后得到的序列。
#  例如:"ABCD"和”BDF“都是"ABCDEFG"的子序列
# 最长公共子序列(LCS)问题：给定两个序列X和Y，求X和Y长度最大的公共子序列
#  例如：X="ABBCBDE" Y="DBBCDB" LCS(X, Y)=BBCD""
# 应用场景：字符串相似度比对
def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]


def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    b = [[0 for _ in range(n+1)] for _ in range(m+1)]  # 1 为左上方，2 为上方，3 为左方
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:  # i, j 位置上匹配的时候，来自于左上方+1
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 1
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 3
    for _ in c:
        print(_)
    return c[m][n], b


def lcs_trackback(x, y):  # 回溯法
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:  # 来自于左上方--> 匹配
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:  # 来自于上方--> 不匹配
            i -= 1
        else:  # b[i][j]==3 来自于左方--> 不匹配
            j -= 1
    return ''.join(reversed(res))


print(lcs_trackback('ABCBDAB', 'DBCABA'))
