def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


def fibnacci_no_recurision(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            s = f[-1] + f[-2]
            f.append(s)
    return f[n]


def second_fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return second_fibnacci(n - 1) + second_fibnacci(n - 2)


def second_fibnacci_no_rec(n):
    li = [0, 1, 1]
    if n > 2:
        for i in range(n-2):
            num = li[-1] + li[-2]
            li.append(num)
    return li[n], li


# print(fibnacci_no_recurision(1))
# print(second_fibnacci(10))
print(second_fibnacci_no_rec(5))
