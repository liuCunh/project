def maxLength(li):
    n = len(li)
    maxLen = [0 for _ in range(n)]
    maxLen[0] = 1
    for i in range(1, n):
        tmp = 0
        for j in range(i):
            if li[i] > li[j] and tmp < maxLen[j]:
                tmp = maxLen[j]
        maxLen[i] = tmp + 1
    return maxLen


user_in = [1, 7, 3, 5, 9, 4, 8]
maxlen = max(maxLength(user_in))
print(maxlen)
