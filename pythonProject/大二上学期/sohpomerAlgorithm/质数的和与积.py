def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def maxPrimeMult(m):
    res = 0
    for i in range(m - 1, -1, -1):
        tmp = m - i
        if isPrime(i) and isPrime(tmp):
            res = max(res, (tmp * i))
    return res
if __name__ == '__main__':
    s = int(input())
    print(maxPrimeMult(s))